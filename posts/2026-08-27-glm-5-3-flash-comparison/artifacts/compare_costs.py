from decimal import Decimal


MODELS = {
    "GLM-5.3-Flash promo": (Decimal("0.075"), Decimal("0.25")),
    "GLM-5.3-Flash list": (Decimal("0.15"), Decimal("0.50")),
    "GLM-5.3": (Decimal("1.40"), Decimal("4.40")),
    "GLM-5.2": (Decimal("1.40"), Decimal("4.40")),
}

INPUT_MILLIONS = Decimal("10")
OUTPUT_MILLIONS = Decimal("2")

print("Scenario: 10M input tokens + 2M output tokens; cache excluded")
for name, (input_price, output_price) in MODELS.items():
    cost = INPUT_MILLIONS * input_price + OUTPUT_MILLIONS * output_price
    print(f"{name}: ${cost:.2f}")

flash_list_cost = INPUT_MILLIONS * MODELS["GLM-5.3-Flash list"][0] + OUTPUT_MILLIONS * MODELS["GLM-5.3-Flash list"][1]
glm_53_cost = INPUT_MILLIONS * MODELS["GLM-5.3"][0] + OUTPUT_MILLIONS * MODELS["GLM-5.3"][1]

print(f"GLM-5.3 / Flash list cost ratio: {glm_53_cost / flash_list_cost:.2f}x")
print(f"Flash list savings vs GLM-5.3: ${glm_53_cost - flash_list_cost:.2f}")
print(f"Input price ratio (GLM-5.3 / Flash list): {MODELS['GLM-5.3'][0] / MODELS['GLM-5.3-Flash list'][0]:.2f}x")
print(f"Output price ratio (GLM-5.3 / Flash list): {MODELS['GLM-5.3'][1] / MODELS['GLM-5.3-Flash list'][1]:.2f}x")
