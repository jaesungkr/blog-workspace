#!/usr/bin/env python3
"""Recalculate the figures used in the Gyeonggi finance explainer."""

import json


general_account_by_field_100m_krw = [
    166_264,
    64_110,
    28_204,
    23_905,
    15_757,
    10_830,
    10_320,
    10_091,
    8_046,
    6_486,
    6_255,
    4_601,
    1_947,
    428,
]

general_account_total = sum(general_account_by_field_100m_krw)
social_welfare = general_account_by_field_100m_krw[0]

result = {
    "sources": {
        "budget_disclosure": "https://www.gg.go.kr/bbs/boardView.do?bIdx=223879621&bsIdx=684&menuId=1954",
        "governor_finance_note": "https://www.gg.go.kr/governor/user/governor/TB00000026/BR00000034",
        "assembly_minutes": "https://kms.ggc.go.kr/cms/mntsViewer.do?mntsId=15608",
    },
    "budget_basis": {
        "fiscal_independence_2022_percent": 55.7,
        "fiscal_independence_2026_percent": 44.4,
        "change_percentage_points": round(44.4 - 55.7, 1),
        "general_account_total_100m_krw": general_account_total,
        "social_welfare_100m_krw": social_welfare,
        "social_welfare_share_percent": round(social_welfare / general_account_total * 100, 1),
        "local_bonds_100m_krw": 5_202,
        "integrated_fiscal_balance_100m_krw": -4_855,
    },
    "province_explanation_2022_to_2026": {
        "acquisition_tax_trillion_krw": [11.0, 8.1],
        "acquisition_tax_change_percent": round((8.1 / 11.0 - 1) * 100, 1),
        "welfare_budget_trillion_krw": [14.0, 19.6],
        "welfare_budget_change_percent": round((19.6 / 14.0 - 1) * 100, 1),
        "scope_note": "Do not directly compare the 19.6 trillion summary with the 16.6264 trillion general-account field without a shared accounting scope.",
    },
    "assembly_speech_7_trillion_composition": {
        "regional_development_fund_trillion_krw": 3.9,
        "fiscal_stabilization_fund_trillion_krw": 1.2,
        "local_bonds_trillion_krw": 1.9,
        "sum_trillion_krw": round(3.9 + 1.2 + 1.9, 1),
        "classification_note": "Composition stated in an assembly speech, not a single audited debt metric.",
    },
}

assert result["budget_basis"]["change_percentage_points"] == -11.3
assert general_account_total == 357_244
assert result["budget_basis"]["social_welfare_share_percent"] == 46.5
assert result["province_explanation_2022_to_2026"]["acquisition_tax_change_percent"] == -26.4
assert result["province_explanation_2022_to_2026"]["welfare_budget_change_percent"] == 40.0
assert result["assembly_speech_7_trillion_composition"]["sum_trillion_krw"] == 7.0

print(json.dumps(result, ensure_ascii=False, indent=2))
