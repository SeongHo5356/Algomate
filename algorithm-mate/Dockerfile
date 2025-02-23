FROM openjdk:17-jdk-slim
WORKDIR /app
COPY build/libs/*.jar app.jar
# 정적 리소스 복사 (필요 시)
COPY src/main/resources/solutions/ /app/resources/solutions/
CMD ["java", "-jar", "app.jar"]
