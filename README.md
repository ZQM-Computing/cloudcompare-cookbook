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

**Status:** Active, public — seeding. Pattern passes land in follow-up work from fleet-verified setups; the tables below list what is planned, not what is already written.

**What this repository is:** CloudCompare patterns — see the table below.

**What it contributes:** Part of the ZQM Computing geospatial portfolio. The umbrella index for the series is [geospatial-cookbooks](https://github.com/ZQM-Computing/geospatial-cookbooks).

**Standing:** This repository is maintained independently. Automated checks cover only the paths and environments configured in its workflows; they do not establish production readiness or operational certification.

## Who this is for

LiDAR and survey practitioners who inspect, align, and compare point clouds.

## Prerequisites

- CloudCompare 2.13.2
- A sample LAS/LAZ file
- Bash for the command-line passes

## Patterns (planned)

| # | Example | What it will demonstrate |
|---|---------|--------------------------|
| 01 | `01-view-filter` | Opening, filtering, and subsampling clouds |
| 02 | `02-registration` | Aligning clouds with ICP and manual picks |
| 03 | `03-cloud-to-cloud` | Cloud-to-cloud distance and change detection |
| 04 | `04-rasterize` | Rasterizing clouds into DEMs and hillshades |

## Repository layout

```text
cloudcompare-cookbook/
├── examples/          # pattern passes, landing in follow-up work
├── README.md
└── LICENSE
```

## Roadmap

- First pattern pass: the first two table rows
- Second pass: the remaining rows, from fleet-verified setups

## Contributing

A contributing guide lands with the first pattern pass. Report security issues to <zqmcomputing@gmail.com> — please do not open a public issue for those.

## More from this series

- [pdal-cookbook](https://github.com/ZQM-Computing/pdal-cookbook) — Point-cloud pipelines, translation, and pgPointCloud ingest
- [pgpointcloud-cookbook](https://github.com/ZQM-Computing/pgpointcloud-cookbook) — Point-cloud storage in Postgres, PDAL ingest, patch queries
- [geoserver-cookbook](https://github.com/ZQM-Computing/geoserver-cookbook) — Publishing, styling, federation, and securing OGC services
