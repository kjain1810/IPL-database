-- MySQL dump 10.13  Distrib 8.0.21, for Linux (x86_64)
--
-- Host: localhost    Database: IPL
-- ------------------------------------------------------
-- Server version	8.0.21-0ubuntu0.20.04.4

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `AllRounder`
--

DROP TABLE IF EXISTS `AllRounder`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `AllRounder` (
  `PlayerID` int DEFAULT NULL,
  `TotalWickets` int DEFAULT '0',
  `CurrentWickets` int DEFAULT '0',
  `TotalRuns` int DEFAULT '0',
  `CurrentRuns` int DEFAULT '0',
  KEY `PlayerID` (`PlayerID`),
  CONSTRAINT `AllRounder_ibfk_1` FOREIGN KEY (`PlayerID`) REFERENCES `Players` (`PlayerID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `AllRounder`
--

LOCK TABLES `AllRounder` WRITE;
/*!40000 ALTER TABLE `AllRounder` DISABLE KEYS */;
/*!40000 ALTER TABLE `AllRounder` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Batsman`
--

DROP TABLE IF EXISTS `Batsman`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Batsman` (
  `TotalRuns` int DEFAULT '0',
  `CurrentRuns` int DEFAULT '0',
  `PlayerID` int DEFAULT NULL,
  KEY `PlayerID` (`PlayerID`),
  CONSTRAINT `Batsman_ibfk_1` FOREIGN KEY (`PlayerID`) REFERENCES `Players` (`PlayerID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Batsman`
--

LOCK TABLES `Batsman` WRITE;
/*!40000 ALTER TABLE `Batsman` DISABLE KEYS */;
/*!40000 ALTER TABLE `Batsman` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Bowler`
--

DROP TABLE IF EXISTS `Bowler`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Bowler` (
  `PlayerID` int DEFAULT NULL,
  `TotalWickets` int DEFAULT '0',
  `CurrentWickets` int DEFAULT '0',
  KEY `PlayerID` (`PlayerID`),
  CONSTRAINT `Bowler_ibfk_1` FOREIGN KEY (`PlayerID`) REFERENCES `Players` (`PlayerID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Bowler`
--

LOCK TABLES `Bowler` WRITE;
/*!40000 ALTER TABLE `Bowler` DISABLE KEYS */;
/*!40000 ALTER TABLE `Bowler` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Matches`
--

DROP TABLE IF EXISTS `Matches`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Matches` (
  `ID` int NOT NULL AUTO_INCREMENT,
  `WinnerID` int NOT NULL,
  `Mom` int NOT NULL,
  `Feild_Umpire1` varchar(80) NOT NULL,
  `Feild_Umpire2` varchar(80) NOT NULL,
  `Stadium_name` varchar(150) NOT NULL,
  `Stadium_city` varchar(40) NOT NULL,
  PRIMARY KEY (`ID`),
  KEY `Winner_team` (`WinnerID`),
  KEY `mom_constraint` (`Mom`),
  KEY `Stadium_name` (`Stadium_name`,`Stadium_city`),
  CONSTRAINT `matches_ibfk_1` FOREIGN KEY (`Stadium_name`, `Stadium_city`) REFERENCES `Stadium` (`Stadium_Name`, `Stadium_City`),
  CONSTRAINT `mom_constraint` FOREIGN KEY (`Mom`) REFERENCES `Players` (`PlayerID`),
  CONSTRAINT `Winner_team` FOREIGN KEY (`WinnerID`) REFERENCES `Teams` (`TeamID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Matches`
--

LOCK TABLES `Matches` WRITE;
/*!40000 ALTER TABLE `Matches` DISABLE KEYS */;
/*!40000 ALTER TABLE `Matches` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Players`
--

DROP TABLE IF EXISTS `Players`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Players` (
  `Name` varchar(80) NOT NULL,
  `Age` int DEFAULT NULL,
  `MoM` int DEFAULT '0',
  `MatchesPlayed` int DEFAULT '0',
  `PlayerID` int NOT NULL AUTO_INCREMENT,
  `TeamID` int DEFAULT NULL,
  PRIMARY KEY (`PlayerID`),
  KEY `TeamID` (`TeamID`),
  CONSTRAINT `Players_ibfk_1` FOREIGN KEY (`TeamID`) REFERENCES `Teams` (`TeamID`),
  CONSTRAINT `Age_positive` CHECK ((`Age` >= 0))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Players`
--

LOCK TABLES `Players` WRITE;
/*!40000 ALTER TABLE `Players` DISABLE KEYS */;
/*!40000 ALTER TABLE `Players` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Plays`
--

DROP TABLE IF EXISTS `Plays`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Plays` (
  `Team_ID` int DEFAULT NULL,
  `Season_Year` int DEFAULT NULL,
  `Match_ID` int DEFAULT NULL,
  `Stadium_name` varchar(150) DEFAULT NULL,
  `Stadium_city` varchar(40) DEFAULT NULL,
  KEY `team_id_foreign` (`Team_ID`),
  KEY `match_id_foreign` (`Match_ID`),
  KEY `Stadium_name` (`Stadium_name`,`Stadium_city`),
  KEY `Season_Year` (`Season_Year`),
  CONSTRAINT `match_id_foreign` FOREIGN KEY (`Match_ID`) REFERENCES `Matches` (`ID`),
  CONSTRAINT `Plays_ibfk_1` FOREIGN KEY (`Stadium_name`, `Stadium_city`) REFERENCES `Stadium` (`Stadium_Name`, `Stadium_City`),
  CONSTRAINT `Plays_ibfk_2` FOREIGN KEY (`Season_Year`) REFERENCES `Seasons` (`Year`),
  CONSTRAINT `team_id_foreign` FOREIGN KEY (`Team_ID`) REFERENCES `Teams` (`TeamID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Plays`
--

LOCK TABLES `Plays` WRITE;
/*!40000 ALTER TABLE `Plays` DISABLE KEYS */;
/*!40000 ALTER TABLE `Plays` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Seasons`
--

DROP TABLE IF EXISTS `Seasons`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Seasons` (
  `Year` int NOT NULL,
  `Finished` tinyint(1) DEFAULT NULL,
  PRIMARY KEY (`Year`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Seasons`
--

LOCK TABLES `Seasons` WRITE;
/*!40000 ALTER TABLE `Seasons` DISABLE KEYS */;
/*!40000 ALTER TABLE `Seasons` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Stadium`
--

DROP TABLE IF EXISTS `Stadium`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Stadium` (
  `Stadium_Name` varchar(150) NOT NULL,
  `Stadium_City` varchar(40) NOT NULL,
  `Max_capacity` int NOT NULL,
  `Home_Team` int NOT NULL,
  PRIMARY KEY (`Stadium_Name`,`Stadium_City`),
  KEY `home_team_fk` (`Home_Team`),
  CONSTRAINT `home_team_fk` FOREIGN KEY (`Home_Team`) REFERENCES `Teams` (`TeamID`),
  CONSTRAINT `capacity_positive` CHECK ((`Max_capacity` > 0))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Stadium`
--

LOCK TABLES `Stadium` WRITE;
/*!40000 ALTER TABLE `Stadium` DISABLE KEYS */;
/*!40000 ALTER TABLE `Stadium` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `TeamManagement`
--

DROP TABLE IF EXISTS `TeamManagement`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `TeamManagement` (
  `TeamID` int DEFAULT NULL,
  `Name` varchar(80) DEFAULT NULL,
  `Role` varchar(80) DEFAULT NULL,
  KEY `TeamID` (`TeamID`),
  CONSTRAINT `TeamManagement_ibfk_1` FOREIGN KEY (`TeamID`) REFERENCES `Teams` (`TeamID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `TeamManagement`
--

LOCK TABLES `TeamManagement` WRITE;
/*!40000 ALTER TABLE `TeamManagement` DISABLE KEYS */;
/*!40000 ALTER TABLE `TeamManagement` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `TeamStandings`
--

DROP TABLE IF EXISTS `TeamStandings`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `TeamStandings` (
  `TeamID` int DEFAULT NULL,
  `SeasonYear` int DEFAULT NULL,
  `Standing` int DEFAULT NULL,
  KEY `TeamID` (`TeamID`),
  KEY `SeasonYear` (`SeasonYear`),
  CONSTRAINT `TeamStandings_ibfk_1` FOREIGN KEY (`TeamID`) REFERENCES `Teams` (`TeamID`),
  CONSTRAINT `TeamStandings_ibfk_2` FOREIGN KEY (`SeasonYear`) REFERENCES `Seasons` (`Year`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `TeamStandings`
--

LOCK TABLES `TeamStandings` WRITE;
/*!40000 ALTER TABLE `TeamStandings` DISABLE KEYS */;
/*!40000 ALTER TABLE `TeamStandings` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Teams`
--

DROP TABLE IF EXISTS `Teams`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Teams` (
  `TeamID` int NOT NULL AUTO_INCREMENT,
  `Name` varchar(80) NOT NULL,
  `CaptainID` int DEFAULT NULL,
  PRIMARY KEY (`TeamID`),
  KEY `CaptainID` (`CaptainID`),
  CONSTRAINT `Teams_ibfk_1` FOREIGN KEY (`CaptainID`) REFERENCES `Players` (`PlayerID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Teams`
--

LOCK TABLES `Teams` WRITE;
/*!40000 ALTER TABLE `Teams` DISABLE KEYS */;
/*!40000 ALTER TABLE `Teams` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-09-29 23:11:11
