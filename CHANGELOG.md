# Changelog

## [Unreleased][]

[Unreleased]: https://github.com/lueurdev/lueur-python-lib/compare/0.22.4..HEAD

## [0.22.4][] - 2025-02-05

[0.22.4]: https://github.com/lueurdev/lueur-python-lib/compare/0.22.3..0.22.4

### Changed

* Do not list gateway/httproute in v1beta1 API

## [0.22.3][] - 2025-02-05

[0.22.3]: https://github.com/lueurdev/lueur-python-lib/compare/0.22.2..0.22.3

### Fixed

* Associate only a single gateway/route per deployment

## [0.22.2][] - 2025-02-03

[0.22.2]: https://github.com/lueurdev/lueur-python-lib/compare/0.22.1..0.22.2

### Fixed

* Added missing credentials parameter

## [0.22.1][] - 2025-02-03

[0.22.1]: https://github.com/lueurdev/lueur-python-lib/compare/0.22.0..0.22.1

### Changed

* Added exceptions management in Kubernetes explore function

## [0.22.0][] - 2025-02-03

[0.22.0]: https://github.com/lueurdev/lueur-python-lib/compare/0.21.0..0.22.0

### Added

* Introducing an id of the target resource in the link. This will eventually
  replace the path and point elements since the id will be more stable
  and faster to lookup
* Pass the Kubernetes clients credentials as a dictionary, otherwise use the
  system credentials
* Build and test against Python 3.13

## [0.21.0][] - 2024-11-03

[0.21.0]: https://github.com/lueurdev/lueur-python-lib/compare/0.20.1..0.21.0

### Fixed

* Minor path fixed in k8s/gateway

## [0.20.1][] - 2024-10-18

[0.20.1]: https://github.com/lueurdev/lueur-python-lib/compare/0.20.0..0.20.1

### Fixed

* Minor path fixed in k8s/gateway

## [0.20.0][] - 2024-10-18

[0.20.0]: https://github.com/lueurdev/lueur-python-lib/compare/0.19.3..0.20.0

### Added

* Initial Grafana support

## [0.19.3][] - 2024-10-17

[0.19.2]: https://github.com/lueurdev/lueur-python-lib/compare/0.19.2..0.19.3

### Fixed

* Pod filtering by service selector labels

## [0.19.2][] - 2024-10-16

### Added

* Links between Gateways and their HTTPRoutes
* Links between service and pods

### Fixed

* Kubernetes is case-sensitive for CRD so transforming HTTPRoutes into
  httproutes

## [0.19.1][] - 2024-10-15

[0.19.1]: https://github.com/lueurdev/lueur-python-lib/compare/0.19.0..0.19.1

### Fixed

* Create pod links

## [0.19.0][] - 2024-10-15

[0.19.0]: https://github.com/lueurdev/lueur-python-lib/compare/0.18.0..0.19.0

### Changed

* Improved links based on communication flow
* New links from nodes to pods and vice versa

## [0.18.0][] - 2024-10-14

[0.18.0]: https://github.com/lueurdev/lueur-python-lib/compare/0.17.1..0.18.0

### Added

* Linking from traced nodes/pods to their resources

## [0.17.1][] - 2024-10-13

[0.17.1]: https://github.com/lueurdev/lueur-python-lib/compare/0.17.0..0.17.1

###  Fixed

* typo

### Changed

* Bumped dependencies

## [0.17.0][] - 2024-10-13

[0.17.0]: https://github.com/lueurdev/lueur-python-lib/compare/0.16.0..0.17.0

### Added

* Conections to the dependnecy flow structure

## [0.16.0][] - 2024-10-12

[0.16.0]: https://github.com/lueurdev/lueur-python-lib/compare/0.15.7..0.16.0

### Added

* Dependency discovery through [k8packet](https://github.com/k8spacket)

## [0.15.7][] - 2024-10-11

[0.15.7]: https://github.com/lueurdev/lueur-python-lib/compare/0.15.6..0.15.7

### Changed

* Better handling of common error responses

## [0.15.6][] - 2024-10-11

[0.15.6]: https://github.com/lueurdev/lueur-python-lib/compare/0.15.5..0.15.6

### Changed

* Better handling of common error responses

## [0.15.5][] - 2024-10-11

[0.15.5]: https://github.com/lueurdev/lueur-python-lib/compare/0.15.4..0.15.5

### Changed

* Tracing and raising Kubernetes client API error

## [0.15.4][] - 2024-10-11

[0.15.4]: https://github.com/lueurdev/lueur-python-lib/compare/0.15.3..0.15.4

### Fixed

* Switch from `status_code` to `status` on the Kubernetes reponse object

## [0.15.3][] - 2024-10-11

[0.15.3]: https://github.com/lueurdev/lueur-python-lib/compare/0.15.2..0.15.3

### Fixed

* Typing for filters

## [0.15.2][] - 2024-10-11

[0.15.2]: https://github.com/lueurdev/lueur-python-lib/compare/0.15.1..0.15.2

### Fixed

* Set default value to None for filters

## [0.15.1][] - 2024-10-10

[0.15.1]: https://github.com/lueurdev/lueur-python-lib/compare/0.15.0..0.15.1

### Added

* Ensures when filter is not set, we allow all targets

## [0.15.0][] - 2024-10-10

[0.15.0]: https://github.com/lueurdev/lueur-python-lib/compare/0.14.15..0.15.0

### Added

* Filtering mechanism to exclude some GCP resources
* Filtering mechanism to exclude some Kubernetes resources

## [0.14.15][] - 2024-10-03

[0.14.15]: https://github.com/lueurdev/lueur-python-lib/compare/0.14.14..0.14.15

### Fixed

* Bad copy paste in dns

## [0.14.14][] - 2024-10-03

[0.14.14]: https://github.com/lueurdev/lueur-python-lib/compare/0.14.13..0.14.14

### Fixed

* Interpolate dns url strings

## [0.14.13][] - 2024-10-03

[0.14.13]: https://github.com/lueurdev/lueur-python-lib/compare/0.14.12..0.14.13

### Fixed

* Force timeout to be ours

## [0.14.12][] - 2024-10-03

[0.14.12]: https://github.com/lueurdev/lueur-python-lib/compare/0.14.11..0.14.12

### Fixed

* Set timeout on all requests

## [0.14.11][] - 2024-10-03

[0.14.11]: https://github.com/lueurdev/lueur-python-lib/compare/0.14.10..0.14.11

### Fixed

* Force timeout

## [0.14.10][] - 2024-10-03

[0.14.10]: https://github.com/lueurdev/lueur-python-lib/compare/0.14.9..0.14.10

### Fixed

* Correct path back to parent

## [0.14.9][] - 2024-10-03

[0.14.9]: https://github.com/lueurdev/lueur-python-lib/compare/0.14.8..0.14.9

### Added

* Use tenacity to perform retries

## [0.14.8][] - 2024-10-03

[0.14.8]: https://github.com/lueurdev/lueur-python-lib/compare/0.14.7..0.14.8

### Fixed

* Use a higher timeout for the gcp client

## [0.14.7][] - 2024-10-03

[0.14.7]: https://github.com/lueurdev/lueur-python-lib/compare/0.14.6..0.14.7

### Fixed

* Fix wrong variable called to retrieve parent

## [0.14.6][] - 2024-10-03

[0.14.6]: https://github.com/lueurdev/lueur-python-lib/compare/0.14.5..0.14.6

### Changed

* Simplified async gcp client

## [0.14.5][] - 2024-10-03

[0.14.5]: https://github.com/lueurdev/lueur-python-lib/compare/0.14.4..0.14.5

### Fixed

* Increase connect GCP client timeout

## [0.14.4][] - 2024-10-03

[0.14.4]: https://github.com/lueurdev/lueur-python-lib/compare/0.14.3..0.14.4

### Fixed

* GCP client timeout default values

## [0.14.3][] - 2024-10-03

[0.14.3]: https://github.com/lueurdev/lueur-python-lib/compare/0.14.2..0.14.3

### Fixed

* GCP client timeout format

## [0.14.2][] - 2024-10-03

[0.14.2]: https://github.com/lueurdev/lueur-python-lib/compare/0.14.1..0.14.2

### Fixed

* Increase GCP client timeout

## [0.14.1][] - 2024-10-03

[0.14.1]: https://github.com/lueurdev/lueur-python-lib/compare/0.14.0..0.14.1

### Fixed

* Correct path back to parent

## [0.14.0][] - 2024-10-03

[0.14.0]: https://github.com/lueurdev/lueur-python-lib/compare/0.13.0..0.14.0

### Added

* DNS support

## [0.13.0][] - 2024-10-03

[0.13.0]: https://github.com/lueurdev/lueur-python-lib/compare/0.12.1..0.13.0

### Added

* Extend links for alerts and slo

## [0.12.1][] - 2024-10-03

[0.12.1]: https://github.com/lueurdev/lueur-python-lib/compare/0.12.0..0.12.1

### Fixed

* Link LB to its subnets

## [0.12.0][] - 2024-10-02

[0.12.0]: https://github.com/lueurdev/lueur-python-lib/compare/0.11.1..0.12.0

### Added

* Link cloudrun to network/subnet
* Link network/subnet to backend service

## [0.11.1][] - 2024-10-02

[0.11.1]: https://github.com/lueurdev/lueur-python-lib/compare/0.11.0..0.11.1

### Fixed

* Deal with no zones found

## [0.11.0][] - 2024-10-02

[0.11.0]: https://github.com/lueurdev/lueur-python-lib/compare/0.10.0..0.11.0

### Added

* Cases where no resources was returned for each API

## [0.10.0][] - 2024-09-25

[0.10.0]: https://github.com/lueurdev/lueur-python-lib/compare/0.9.5..0.10.0

### Changed

* Reworked some categories

## [0.9.5][] - 2024-09-25

[0.9.5]: https://github.com/lueurdev/lueur-python-lib/compare/0.9.4..0.9.5

### Fixed

* Log when no compute instances were returned

## [0.9.4][] - 2024-09-25

[0.9.4]: https://github.com/lueurdev/lueur-python-lib/compare/0.9.3..0.9.4

### Fixed

* Log when no memorystore instances were returned

## [0.9.3][] - 2024-09-25

[0.9.3]: https://github.com/lueurdev/lueur-python-lib/compare/0.9.2..0.9.3

### Fixed

* Log when a warning is raised during listing instances

## [0.9.2][] - 2024-09-25

[0.9.2]: https://github.com/lueurdev/lueur-python-lib/compare/0.9.1..0.9.2

### Fixed

* Move task group result loop outside the context manager of the taskgroup

## [0.9.1][] - 2024-09-25

[0.9.1]: https://github.com/lueurdev/lueur-python-lib/compare/0.9.0..0.9.1

### Fixed

* Add storage query parameter to request

## [0.9.0][] - 2024-09-25

[0.9.0]: https://github.com/lueurdev/lueur-python-lib/compare/0.8.3..0.9.0

### Added

* memorystore, storage and compute basic support for GCP

## [0.8.3][] - 2024-09-12

[0.8.3]: https://github.com/lueurdev/lueur-python-lib/compare/0.8.2..0.8.3

### Fixed

* Point to resource object to get path and pointer

## [0.8.2][] - 2024-09-12

[0.8.2]: https://github.com/lueurdev/lueur-python-lib/compare/0.8.1..0.8.2

### Fixed

* Github action version for upload/download artifacts

## [0.8.1][] - 2024-09-12

[0.8.1]: https://github.com/lueurdev/lueur-python-lib/compare/0.8.0..0.8.1

### Fixed

* Point to resource object to get path and pointer

## [0.8.0][] - 2024-09-11

[0.8.0]: https://github.com/lueurdev/lueur-python-lib/compare/0.7.0..0.8.0

### Changed

* The `application` and `service` categories as they were poorly defined

## [0.7.0][] - 2024-09-10

[0.7.0]: https://github.com/lueurdev/lueur-python-lib/compare/0.6.2..0.7.0

### Added

* The category field in the meta

## [0.6.2][] - 2024-09-07

[0.6.2]: https://github.com/lueurdev/lueur-python-lib/compare/0.6.1..0.6.2

### Fixed

* Fix the gateway link path to cloudruns

## [0.6.1][] - 2024-09-07

[0.6.1]: https://github.com/lueurdev/lueur-python-lib/compare/0.6.0..0.6.1

### Fixed

* Fix the gateway link path to urlmaps

## [0.6.0][] - 2024-09-06

[0.6.0]: https://github.com/lueurdev/lueur-python-lib/compare/0.5.1..0.6.0

### Added

* Kubernetes expand_links

## [0.5.1][] - 2024-09-06

[0.5.1]: https://github.com/lueurdev/lueur-python-lib/compare/0.5.0..0.5.1

### Fixed

* ReplicaSet and Deployment links queries

## [0.5.0][] - 2024-09-06

[0.5.0]: https://github.com/lueurdev/lueur-python-lib/compare/0.4.2..0.5.0

### Added

* Extended GCP and Kubernetes support

## [0.4.2][] - 2024-09-05

[0.4.2]: https://github.com/lueurdev/lueur-python-lib/compare/0.4.1..0.4.2

### Fixed

* Export meta for AWS and Kubernetes

## [0.4.1][] - 2024-09-05

[0.4.1]: https://github.com/lueurdev/lueur-python-lib/compare/0.4.0..0.4.1

### Fixed

* Amend from `k8s/service` to `service`

## [0.4.0][] - 2024-09-05

[0.4.0]: https://github.com/lueurdev/lueur-python-lib/compare/0.3.1..0.4.0

### Changed

* Bump dependencies
* Extend each platform metadata

## [0.3.1][] - 2024-07-16

[0.3.1]: https://github.com/lueurdev/lueur-python-lib/compare/0.3.0..0.3.1

### Fixed

* Add display to Kubernetes meta

## [0.3.0][] - 2024-07-01

[0.3.0]: https://github.com/lueurdev/lueur-python-lib/compare/0.2.0..0.3.0

### Added

* First API package (will likely evolve quite a bit)

## [0.2.0][] - 2024-06-26

[0.2.0]: https://github.com/lueurdev/lueur-python-lib/compare/0.1.0..0.2.0

### Added

* Pass explicit credentials to GCP when needed by caller

## [0.1.0][] - 2024-06-26

[0.1.0]: https://github.com/lueurdev/lueur-python-lib/tree/0.1.0

### Added

* Initial release
