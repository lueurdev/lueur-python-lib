# Changelog

## [Unreleased][]

[Unreleased]: https://github.com/lueurdev/lueur/compare/0.14.4..HEAD

## [0.14.4][] - 2024-10-03

[0.14.4]: https://github.com/lueurdev/lueur/compare/0.14.3..0.14.4

### Fixed

-   GCP client timeout default values

## [0.14.3][] - 2024-10-03

[0.14.3]: https://github.com/lueurdev/lueur/compare/0.14.2..0.14.3

### Fixed

-   GCP client timeout format

## [0.14.2][] - 2024-10-03

[0.14.2]: https://github.com/lueurdev/lueur/compare/0.14.1..0.14.2

### Fixed

-   Increase GCP client timeout

## [0.14.1][] - 2024-10-03

[0.14.1]: https://github.com/lueurdev/lueur/compare/0.14.0..0.14.1

### Fixed

-   Correct path back to parent

## [0.14.0][] - 2024-10-03

[0.14.0]: https://github.com/lueurdev/lueur/compare/0.13.0..0.14.0

### Added

-   DNS support

## [0.13.0][] - 2024-10-03

[0.13.0]: https://github.com/lueurdev/lueur/compare/0.12.1..0.13.0

### Added

-   Extend links for alerts and slo

## [0.12.1][] - 2024-10-03

[0.12.1]: https://github.com/lueurdev/lueur/compare/0.12.0..0.12.1

### Fixed

-   Link LB to its subnets

## [0.12.0][] - 2024-10-02

[0.12.0]: https://github.com/lueurdev/lueur/compare/0.11.1..0.12.0

### Added

-   Link cloudrun to network/subnet
-   Link network/subnet to backend service

## [0.11.1][] - 2024-10-02

[0.11.1]: https://github.com/lueurdev/lueur/compare/0.11.0..0.11.1

### Fixed

-   Deal with no zones found

## [0.11.0][] - 2024-10-02

[0.11.0]: https://github.com/lueurdev/lueur/compare/0.10.0..0.11.0

### Added

-   Cases where no resources was returned for each API

## [0.10.0][] - 2024-09-25

[0.10.0]: https://github.com/lueurdev/lueur/compare/0.9.5..0.10.0

### Changed

-   Reworked some categories

## [0.9.5][] - 2024-09-25

[0.9.5]: https://github.com/lueurdev/lueur/compare/0.9.4..0.9.5

### Fixed

-   Log when no compute instances were returned

## [0.9.4][] - 2024-09-25

[0.9.4]: https://github.com/lueurdev/lueur/compare/0.9.3..0.9.4

### Fixed

-   Log when no memorystore instances were returned

## [0.9.3][] - 2024-09-25

[0.9.3]: https://github.com/lueurdev/lueur/compare/0.9.2..0.9.3

### Fixed

-   Log when a warning is raised during listing instances

## [0.9.2][] - 2024-09-25

[0.9.2]: https://github.com/lueurdev/lueur/compare/0.9.1..0.9.2

### Fixed

-   Move task group result loop outside the context manager of the taskgroup

## [0.9.1][] - 2024-09-25

[0.9.1]: https://github.com/lueurdev/lueur/compare/0.9.0..0.9.1

### Fixed

-   Add storage query parameter to request

## [0.9.0][] - 2024-09-25

[0.9.0]: https://github.com/lueurdev/lueur/compare/0.8.3..0.9.0

### Added

-   memorystore, storage and compute basic support for GCP

## [0.8.3][] - 2024-09-12

[0.8.3]: https://github.com/lueurdev/lueur/compare/0.8.2..0.8.3

### Fixed

-   Point to resource object to get path and pointer

## [0.8.2][] - 2024-09-12

[0.8.2]: https://github.com/lueurdev/lueur/compare/0.8.1..0.8.2

### Fixed

-   Github action version for upload/download artifacts

## [0.8.1][] - 2024-09-12

[0.8.1]: https://github.com/lueurdev/lueur/compare/0.8.0..0.8.1

### Fixed

-   Point to resource object to get path and pointer

## [0.8.0][] - 2024-09-11

[0.8.0]: https://github.com/lueurdev/lueur/compare/0.7.0..0.8.0

### Changed

-   The `application` and `service` categories as they were poorly defined

## [0.7.0][] - 2024-09-10

[0.7.0]: https://github.com/lueurdev/lueur/compare/0.6.2..0.7.0

### Added

-   The category field in the meta

## [0.6.2][] - 2024-09-07

[0.6.2]: https://github.com/lueurdev/lueur/compare/0.6.1..0.6.2

### Fixed

-   Fix the gateway link path to cloudruns

## [0.6.1][] - 2024-09-07

[0.6.1]: https://github.com/lueurdev/lueur/compare/0.6.0..0.6.1

### Fixed

-   Fix the gateway link path to urlmaps

## [0.6.0][] - 2024-09-06

[0.6.0]: https://github.com/lueurdev/lueur/compare/0.5.1..0.6.0

### Added

-   Kubernetes expand_links

## [0.5.1][] - 2024-09-06

[0.5.1]: https://github.com/lueurdev/lueur/compare/0.5.0..0.5.1

### Fixed

-   ReplicaSet and Deployment links queries

## [0.5.0][] - 2024-09-06

[0.5.0]: https://github.com/lueurdev/lueur/compare/0.4.2..0.5.0

### Added

-   Extended GCP and Kubernetes support

## [0.4.2][] - 2024-09-05

[0.4.2]: https://github.com/lueurdev/lueur/compare/0.4.1..0.4.2

### Fixed

-   Export meta for AWS and Kubernetes

## [0.4.1][] - 2024-09-05

[0.4.1]: https://github.com/lueurdev/lueur/compare/0.4.0..0.4.1

### Fixed

-   Amend from `k8s/service` to `service`

## [0.4.0][] - 2024-09-05

[0.4.0]: https://github.com/lueurdev/lueur/compare/0.3.1..0.4.0

### Changed

-   Bump dependencies
-   Extend each platform metadata

## [0.3.1][] - 2024-07-16

[0.3.1]: https://github.com/lueurdev/lueur/compare/0.3.0..0.3.1

### Fixed

-   Add display to Kubernetes meta

## [0.3.0][] - 2024-07-01

[0.3.0]: https://github.com/lueurdev/lueur/compare/0.2.0..0.3.0

### Added

-   First API package (will likely evolve quite a bit)

## [0.2.0][] - 2024-06-26

[0.2.0]: https://github.com/lueurdev/lueur/compare/0.1.0..0.2.0

### Added

-   Pass explicit credentials to GCP when needed by caller

## [0.1.0][] - 2024-06-26

[0.1.0]: https://github.com/lueurdev/lueur/tree/0.1.0

### Added

-   Initial release
