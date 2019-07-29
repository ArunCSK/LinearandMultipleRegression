

val kafkaBrokers = "10.0.0.11:9092,10.0.0.15:9092,10.0.0.12:9092"

// Setup connection to Kafka
val kafka = spark.readStream
  .format("kafka")
  .option("kafka.bootstrap.servers", kafkaBrokers)
  .option("subscribe", "azurefeedback")   
  .option("startingOffsets", "latest")
  .load() 