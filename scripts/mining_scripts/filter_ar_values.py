# Filter architectural rule violation values

import json
import pandas

columns = [ 'projectKey', 'total_issues', 'design_issues', 
'squid:S3422', 'squid:S2975', 'squid:S2638', 'squid:S2221', 'squid:S2166', 
'squid:S2157', 'squid:S2147', 'squid:S2134', 'squid:S2068', 'squid:S1696', 
'squid:S1610', 'squid:S1609', 'squid:S1598', 'squid:S1226', 'squid:S1199', 
'squid:S1193', 'squid:S1188', 'squid:S1182', 'squid:S1181', 'squid:S1166', 
'squid:S1165', 'squid:S1163', 'squid:S1161', 'squid:S106', 'squid:S00107', 
'squid:S00104', 'squid:MethodCyclomaticComplexity', 
'squid:ClassVariableVisibilityCheck', 'squid:ClassCyclomaticComplexity', 
'jproperties:maximum-number-keys', 'squid:S1695', 'squid:S1160', 'squid:S2059', 
'squid:S2693', 'squid:S2438', 'squid:S1118', 'squid:S3398', 'squid:S2062', 
'squid:S2077', 'squid:S2095', 'javascript:Eval', 
'squid:ClassVariableVisibilityCheck', 'squid:ObjectFinalizeOverridenCheck', 
'squid:RedundantThrowsDeclarationCheck', 'squid:S00112', 'squid:S1118', 
'squid:S1133', 'squid:S1148', 'squid:S1170', 'squid:S1182', 'squid:S1185', 
'squid:S1192', 'squid:S1194', 'squid:S1210', 'squid:S1214', 'squid:S1217', 
'squid:S1220', 'squid:S1221', 'squid:S1301', 'squid:S1313', 'squid:S1444', 
'squid:S1488', 'squid:S1848', 'squid:S1860', 'squid:S1862', 'squid:S1872', 
'squid:S1873', 'squid:S2142', 'squid:S2147', 'squid:S2236', 'squid:S2273', 
'squid:S2276', 'squid:S2386', 'squid:S2696', 'squid:S2737', 
'squid:S2885', 'squid:S2222']

columns = [ 'projectKey', 'total_issues', 'design_issues', 'ClassComplexity']

design_rules = columns[3:len(columns)]

dataframe = pandas.DataFrame(0, index= range(15000), columns = columns)

index = 0

print('Loading dataset...')
with open('issues.json') as json_file:  
    data = json.load(json_file)
    
    print('Dataset loaded!')

    index += 1

    # Iterate through each project in dataset
    for p in data:

        print('Project', index, ':', p['projectKey'])
        
        total_issues = 0
        design_issues = 0

        # Iterate through each issue in the project
        for issue in p['issues']:

            total_issues += 1

            print('Project', index, ':', p['projectKey'], '| Total issues:', total_issues)

            # Identify if rule is design rule (defined in columns), and in 
            # case add +1 for each rule in respective column
            if issue['rule'] in design_rules:
                dataframe.loc[index, issue['rule']] += 1
                design_issues += 1

        dataframe.loc[index, 'projectKey'] = p['projectKey']
        dataframe.loc[index, 'total_issues'] = total_issues
        dataframe.loc[index, 'design_issues'] = design_issues

        # increment dataframe index for next project
        index += 1

print('Started saving csv')
dataframe.to_csv('filtered_dataset.csv', header = True)
