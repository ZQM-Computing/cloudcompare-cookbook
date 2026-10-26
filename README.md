# CloudCompare Cookbook

<!-- ZQM-START -->
<!-- markdownlint-disable MD033 -->
<p align="center">
  <strong>ZQM Computing — Geospatial Engineering & Scientific Computing</strong><br>
  <a href="https://github.com/ZQM-Computing">ZQM Computing</a>
</p>
<!-- markdownlint-enable MD033 -->
<!-- ZQM-END -->

![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)

A **CloudCompare cookbook** for point-cloud visualization, registration, and comparison. Patterns are drawn from the ZQM fleet's CloudCompare 2.13.2 installs on all three Windows nodes. It is intended for LiDAR and survey practitioners who inspect, align, and compare point clouds. Validate each pattern against your own data, software versions, and operating environment before adopting it.

## Repository role and status

**Status:** Active, public — first CLI-inspection pattern written. CI validates the shell contract; runtime behavior still requires a fleet run against CloudCompare 2.13.2.

**What this repository is:** CloudCompare patterns — see the table below.

**What it contributes:** Part of the ZQM Computing geospatial portfolio. The umbrella index for the series is [geospatial-cookbooks](https://github.com/ZQM-Computing/geospatial-cookbooks).

**Standing:** This repository is maintained independently. Automated checks cover only the paths and environments configured in its workflows; they do not establish production readiness or operational certification.

## Who this is for

LiDAR and survey practitioners who inspect, align, and compare point clouds.

## Prerequisites

- CloudCompare 2.13.2
- A sample LAS/LAZ file
- Bash for the command-line passes

## Patterns

| # | Example | Status | What it demonstrates |
|---|---------|--------|---------------------|
| 01 | [01-cli-basics](examples/01-cli-basics/README.md) | Written; runtime check pending | Capture CloudCompare CLI help output with a bounded timeout and confirm the command-line interface responds |
| 02 | `02-registration` | Planned | Aligning clouds with ICP and manual picks |
| 03 | `03-cloud-to-cloud` | Planned | Cloud-to-cloud distance and change detection |
| 04 | `04-rasterize` | Planned | Rasterizing clouds into DEMs and hillshades |

The pattern inventory above is authoritative: planned patterns are marked **Planned** and are not presented as implemented examples. Pattern numbers are unique and reserved for future directories.

## Repository layout

```text
cloudcompare-cookbook/
├── examples/01-cli-basics/  # bounded CLI inspection script
├── tests/             # static script/documentation contracts
├── .github/workflows/ # CI
├── README.md
└── LICENSE
```

## Roadmap

- Run the bounded CLI-inspection pattern against the fleet CloudCompare 2.13.2 executable and capture its actual help output.
- Verify the help timeout and executable path behavior on Windows Git Bash before relying on GNU `timeout`.
- Add point-cloud open/export, filtering, and registration patterns only after command-line flags and output files are verified on Windows.

## Contributing

A contributing guide lands with the first pattern pass. Report security issues to <zqmcomputing@gmail.com> — please do not open a public issue for those.

## More from this series

- [pdal-cookbook](https://github.com/ZQM-Computing/pdal-cookbook) — Point-cloud pipelines, translation, and pgPointCloud ingest
- [pgpointcloud-cookbook](https://github.com/ZQM-Computing/pgpointcloud-cookbook) — Point-cloud storage in Postgres, PDAL ingest, patch queries
- [geoserver-cookbook](https://github.com/ZQM-Computing/geoserver-cookbook) — Publishing, styling, federation, and securing OGC services
