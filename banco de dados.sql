CREATE DATABASE  IF NOT EXISTS `sistema-de-eventos` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `sistema-de-eventos`;
-- MySQL dump 10.13  Distrib 8.0.30, for Win64 (x86_64)
--
-- Host: localhost    Database: sistema-de-eventos
-- ------------------------------------------------------
-- Server version	8.0.27

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `avaliacao`
--

DROP TABLE IF EXISTS `avaliacao`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `avaliacao` (
  `id` int NOT NULL AUTO_INCREMENT,
  `Nome` varchar(45) NOT NULL,
  `Evento` varchar(45) NOT NULL,
  `Estrelas` int NOT NULL,
  `Comentario` varchar(250) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `avaliacao`
--

LOCK TABLES `avaliacao` WRITE;
/*!40000 ALTER TABLE `avaliacao` DISABLE KEYS */;
INSERT INTO `avaliacao` VALUES (1,'luana','Evento teste',5,'Evento muito legal'),(2,'Matheus','Evento teste',5,'Evento interessante'),(3,'Matheus Santos','Teste',5,'Evento de teste legal');
/*!40000 ALTER TABLE `avaliacao` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `eventos`
--

DROP TABLE IF EXISTS `eventos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `eventos` (
  `id` int NOT NULL AUTO_INCREMENT,
  `Nome` varchar(75) NOT NULL,
  `Inicio` date NOT NULL,
  `Termino` date NOT NULL,
  `Hora_inicio` time NOT NULL,
  `Hora_termino` time NOT NULL,
  `Local` varchar(45) NOT NULL,
  `Descricao` varchar(250) NOT NULL,
  `Vagas` int NOT NULL,
  `Categoria` varchar(45) NOT NULL,
  `status` varchar(45) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=26 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `eventos`
--

LOCK TABLES `eventos` WRITE;
/*!40000 ALTER TABLE `eventos` DISABLE KEYS */;
INSERT INTO `eventos` VALUES (1,'Evento teste','2023-06-27','2023-06-27','10:00:00','11:00:00','São Paulo','Evento para teste de sistema',1,'A','Concluido'),(2,'Evento teste 2','2023-06-28','2023-06-28','10:00:00','11:00:00','São Paulo','Evento para teste de sistema',2,'A','Cancelado'),(3,'Teste','2023-06-28','2023-06-28','12:00:00','22:00:00','Aracaju','evento cadastrado para teste',9,'A','Cancelado'),(4,'Evento novo de teste','2023-07-02','2023-07-02','13:00:00','19:00:00','Aracaju','evento para teste',12,'C','Concluído'),(5,'Evento ok','2023-07-02','2023-07-02','13:00:00','19:00:00','Nossa Senhora do Socorro','teste',2,'B','Concluído');
/*!40000 ALTER TABLE `eventos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `inscritos`
--

DROP TABLE IF EXISTS `inscritos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `inscritos` (
  `id` int NOT NULL AUTO_INCREMENT,
  `Nome` varchar(75) NOT NULL,
  `Evento` varchar(45) NOT NULL,
  `Presenca` varchar(45) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `inscritos`
--

LOCK TABLES `inscritos` WRITE;
/*!40000 ALTER TABLE `inscritos` DISABLE KEYS */;
INSERT INTO `inscritos` VALUES (1,'Matheus','Evento teste','true'),(2,'Matheus Santos','Teste','true'),(3,'Marcos Vinicius Santos Ferro','Teste','true');
/*!40000 ALTER TABLE `inscritos` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-07-09 21:02:15
