from decimal import Decimal as D
import json
rows={"Fable 5.1":(10,50),"Fable 5.2":(8,40),"Fable 5.2 fast":(16,80),"Opus 5.5":(4,20)}
result={"actor":"Codex arithmetic audit, no model execution", "date":"2026-11-10", "input_tokens":100000,"output_tokens":10000,"excluded":"cache, tools, retries, subscriptions", "fixed_usage_cost_usd":{k:float(D(i)*D('0.1')+D(o)*D('0.01')) for k,(i,o) in rows.items()},"base_price_reduction_percent":float((D(10)-D(8))/D(10)*100),"frontiercode_gain_percentage_points":float(D('49.1')-D('32.4')),"frontierswe_gain_percentage_points":float(D('69.9')-D('56.3')),"aa_high_to_max_index_gain":65-62,"aa_high_to_max_cost_ratio":float(D('26.54')/D('9.08')),"aa_high_to_max_time_ratio":float(D('46.4')/D('17.7'))}
result['frontiercode_vs_opus_percentage_points']=float(D('49.1')-D('45.5'))
result['frontierswe_vs_opus_percentage_points']=float(D('69.9')-D('62.3'))
assert result['frontiercode_vs_opus_percentage_points']==3.6
assert result['frontierswe_vs_opus_percentage_points']==7.6
assert result['fixed_usage_cost_usd']=={'Fable 5.1':1.5,'Fable 5.2':1.2,'Fable 5.2 fast':2.4,'Opus 5.5':0.6}
print(json.dumps(result,ensure_ascii=False,indent=2))
