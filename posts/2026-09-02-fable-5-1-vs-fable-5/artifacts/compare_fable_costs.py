from decimal import Decimal


BASE_INPUT_PRICE = Decimal("10")
CACHE_WRITE_PRICE = Decimal("12.5")
OUTPUT_PRICE = Decimal("50")


def cost(cache_read_price: Decimal, cache_read_tokens_m: Decimal) -> Decimal:
    cache_write_tokens_m = Decimal("0.2")
    uncached_input_tokens_m = Decimal("0.1")
    output_tokens_m = Decimal("0.1")
    return (
        cache_write_tokens_m * CACHE_WRITE_PRICE
        + cache_read_tokens_m * cache_read_price
        + uncached_input_tokens_m * BASE_INPUT_PRICE
        + output_tokens_m * OUTPUT_PRICE
    )


scenarios = {
    "short": Decimal("4"),
    "long": Decimal("10"),
}

for name, cache_read_tokens_m in scenarios.items():
    fable_5 = cost(Decimal("1"), cache_read_tokens_m)
    fable_5_1 = cost(Decimal("0.25"), cache_read_tokens_m)
    savings = (fable_5 - fable_5_1) / fable_5 * Decimal("100")
    print(
        f"{name}: cache_read={cache_read_tokens_m}M, "
        f"fable_5=${fable_5:.2f}, fable_5_1=${fable_5_1:.2f}, "
        f"savings={savings:.1f}%"
    )

