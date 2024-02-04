---
title: Java
created: 2024-01-15T15:26:18-08:00
updated: 2024-02-04T07:37:07-08:00
---

Enterprise object-oriented [Programming Language](Programming%20Language.md).

On my system, mostly managing with [SDKMAN](SDKMAN.md).

## JDK Distributions

* [JDK Distributions - SDKMAN! the Software Development Kit Manager](https://sdkman.io/jdks)
* [Which Version of JDK Should I Use? | whichjdk.com](https://whichjdk.com)

Some focus on distinct capabilities such as better performance on desktop. Some are just "this is the JDK you get on our platform." No, I can't really tell the difference. [Minecraft](Minecraft.md) behaves a little better for me under Temurin on Linux. That's about all I know so far.

* [Corretto - Amazon](https://aws.amazon.com/corretto/?filtered-posts.sort-by=item.additionalFields.createdDate&filtered-posts.sort-order=desc)
* [Dragonwell - Alibaba](https://dragonwell-jdk.io/#/index)
* [GraalVM](https://www.graalvm.org)
  * GraalVM Oracle
  * GrallVM Community
* [Java SE Development Kit - Oracle](https://www.oracle.com/java/)
* [Kona - Tencent](https://github.com/Tencent/TencentKona-8)
* [Liberica - Bellsoft](https://bell-sw.com)
* [Liberica NIK - Bellsoft](https://bell-sw.com/liberica-native-image-kit/)
  * Native Image Kit
* [Mandrel - Red Hat](https://github.com/graalvm/mandrel)
* [OpenJDK - jdk.java.net](https://jdk.java.net)
* [OpenJDK - Microsoft](https://www.microsoft.com/openjdk)
* [SapMachine - SAP](https://sap.github.io/SapMachine/)
* [Semeru - IBM](https://developer.ibm.com/languages/java/semeru-runtimes/)
* [Temurin - Eclipse](https://projects.eclipse.org/projects/adoptium.temurin)
* [Trava - Trava](https://github.com/TravaOpenJDK/trava-jdk-11-dcevm)
* [Zulu - Azul Systems](https://www.azul.com/downloads/?package=jdk#zulu)

## LTS Releases

* [Java version history - Wikipedia](https://en.wikipedia.org/wiki/Java_version_history)

|Version|Release Date|Notes|
|-------|------------|-----|
|Java SE 8|2014-03-18|...|
|Java SE 11|2018-09-25|...|
|Java SE 17|2021-09-14|...|
|Java SE 21|2023-09-19||

I was going to add an *EOL* column but every JDK distribution has its own support calendar. For example, Oracle stopped commercial support for JDK 8 in 2022, while Azul will support it until the end of 2030.

## Managing Projects

Gradle or Maven

### Maven

[Maven – Introduction](https://maven.apache.org/what-is-maven.html)

* reduce details needed for build process
* provide a uniform build system
* Standardize project definitions
* encourage better development practices

### Gradle

[Gradle | Gradle vs Maven Comparison](https://gradle.org/maven-vs-gradle/)

* flexible
* reduce build time
* improve user experience
* support more complex dependency rules for composite builds

Build time savings is through incremental builds, so maybe *worse* numbers in CI context? #question

## Related

* https://www.java.com/
