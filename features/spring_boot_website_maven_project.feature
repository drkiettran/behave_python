Feature: Can create a Spring Boot Maven project with an available release
  As a Spring Boot user,
  I want to create a Maven based project using Spring Boot framework
  So that I can create application quickly for must customer

@maven_project
Scenario: Can create Maven Project for Spring Boot 2.2.8
  Given I am at the Spring Initializer website "https://start.spring.io/"
  When I create a Spring boot with the following attributes:
    | project | language | version | group          | artifact  | description | packaging | java_version |
    | Maven   | Kotlin   | 2.2.8   | com.drkiettran | my_kotlin | testing     | war       | 11           |
  Then I should receive a zip file
  And the file should contain a build.gradle file with version "2.2.8"
