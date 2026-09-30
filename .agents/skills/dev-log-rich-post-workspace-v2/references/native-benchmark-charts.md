# Native benchmark charts

Use a fenced `benchmark-chart` JSON object when a source-based comparison
needs visible bars without a raster upload. The renderer emits a semantic
figure with text labels, percentages, task costs, and an evidence caption.
It uses no JavaScript or external resource.

Required fields are `title`, `caption`, and `groups`. Each group has a `label`
and `rows`; each row has `model`, numeric `score`, numeric `cost`, and optional
`tone` (`sol`, `opus`, `astra`, or `neutral`). Scores must be finite percentages
between 0 and 100, and USD task costs must be finite and nonnegative.

Use only metrics where a higher percentage is better. The bar scale always
starts at zero and ends at 100. An error rate belongs in a labeled table,
not this component. Identify the source, exact effort setting, fallback
conditions, and reconstruction in or beside the caption. A reconstruction
must never be presented as an original benchmark run.

The native figure is part of the page layout. Inspect the complete figure,
text/data agreement, and mobile wrapping during creator preflight and the
independent final page gate. It does not create a new Tistory media-upload item.
