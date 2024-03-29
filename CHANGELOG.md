CHANGELOG
==========
## 0.0.2 - 2016-03-03
### Added
- Parser Results model
- Parser Results api endpoints
- AuditFields mixin serializer
- Add a regex for the date

## 0.0.3 - 2016-03-04
### Added
- Serializer to handle Book Commands
- Include data and rest-framework templates in MANIFEST.in
- Add dateutils to parse dates

## 0.0.4 - 2016-03-13
### Added
- Add tx files to MANIFEST

## 0.0.5 - 2016-03-13
### Changed
- The location of static files folder

## 0.0.6 - 2016-03-13
### Changed
- Set the Debug settings variable from the env

### Added
- Playbook to deploy the api

## 0.0.7 - 2016-03-13
### Added
-  Variable to the env for the static files path during production

## 0.0.8 - 2016-03-13
### Added
- Static file to the MANIFEST.in

## 0.0.9 - 2016-03-15
### Added
- Reset the migrations
- Added RouteTree and Route models
- Default data for airlines and airports

### Changed
- The Airline and Airport models


## 0.0.10 - 2016-03-27
### Added
- Default data for the application, RouteTree
- Me endpoint for user details


## 0.0.11 - 2016-04-25
### Added
- Add QPX Express API
- Remove default data for routes
- Add City lookup


## 0.0.12 - 2016-05-02
### Added
- A user can book a flight
- Fix form CSRF and parsing errors

### Removes
- Models in Airline and Booking app


## 0.0.13 - 2016-05-08
- Resets migrations
- Add parser endpoints for graph generation


## 0.0.14 - 2016-05-08
- Bug fixes: Parser correctness

## 0.0.15 - 2016-05-08
- Overide user serializer to allow new users to be created

## 0.0.16 - 2016-05-17
- Add show my booked flights command
- Edit book command to allow search by price and to specify a return date

## 0.0.16 - 2016-05-18
- Add actions parameter to the user fields

## 0.0.17 - 2016-05-20
- Add command for adults
- Special endpoints for parser results
