-- MariaDB dump 10.17  Distrib 10.5.5-MariaDB, for Linux (x86_64)
--
-- Host: localhost    Database: IPL
-- ------------------------------------------------------
-- Server version	10.5.5-MariaDB

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
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
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `AllRounder` (
  `PlayerID` int(11) DEFAULT NULL,
  `TotalWickets` int(11) DEFAULT 0,
  `CurrentWickets` int(11) DEFAULT 0,
  `TotalRuns` int(11) DEFAULT 0,
  `CurrentRuns` int(11) DEFAULT 0,
  KEY `PlayerID` (`PlayerID`),
  CONSTRAINT `AllRounder_ibfk_1` FOREIGN KEY (`PlayerID`) REFERENCES `Players` (`PlayerID`),
  CONSTRAINT `AllRounder_AllRunsNonNeg` CHECK (`CurrentRuns` >= 0 and `TotalRuns` >= 0),
  CONSTRAINT `AllRounder_RunsNonNeg` CHECK (`CurrentWickets` >= 0 and `TotalWickets` >= 0)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `AllRounder`
--

LOCK TABLES `AllRounder` WRITE;
/*!40000 ALTER TABLE `AllRounder` DISABLE KEYS */;
INSERT INTO `AllRounder` VALUES (11,2,0,2,0),(21,3,0,3,0),(29,2,0,2,0),(30,2,0,2,0);
/*!40000 ALTER TABLE `AllRounder` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Batsman`
--

DROP TABLE IF EXISTS `Batsman`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Batsman` (
  `TotalRuns` int(11) DEFAULT 0,
  `CurrentRuns` int(11) DEFAULT 0,
  `PlayerID` int(11) DEFAULT NULL,
  KEY `PlayerID` (`PlayerID`),
  CONSTRAINT `Batsman_ibfk_1` FOREIGN KEY (`PlayerID`) REFERENCES `Players` (`PlayerID`),
  CONSTRAINT `Batsman_RunsNonNeg` CHECK (`CurrentRuns` >= 0 and `TotalRuns` >= 0)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Batsman`
--

LOCK TABLES `Batsman` WRITE;
/*!40000 ALTER TABLE `Batsman` DISABLE KEYS */;
INSERT INTO `Batsman` VALUES (2,0,8),(3,0,9),(3,0,15),(3,0,16),(3,0,17),(3,0,18),(3,0,19),(3,0,23),(2,0,24),(2,0,25),(2,0,26),(2,0,27);
/*!40000 ALTER TABLE `Batsman` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Bowler`
--

DROP TABLE IF EXISTS `Bowler`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Bowler` (
  `PlayerID` int(11) DEFAULT NULL,
  `TotalWickets` int(11) DEFAULT 0,
  `CurrentWickets` int(11) DEFAULT 0,
  KEY `PlayerID` (`PlayerID`),
  CONSTRAINT `Bowler_ibfk_1` FOREIGN KEY (`PlayerID`) REFERENCES `Players` (`PlayerID`),
  CONSTRAINT `Bowler_RunsNonNeg` CHECK (`CurrentWickets` >= 0 and `TotalWickets` >= 0)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Bowler`
--

LOCK TABLES `Bowler` WRITE;
/*!40000 ALTER TABLE `Bowler` DISABLE KEYS */;
INSERT INTO `Bowler` VALUES (10,2,0),(12,2,0),(14,3,0),(20,3,0),(22,3,0),(28,2,0);
/*!40000 ALTER TABLE `Bowler` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Matches`
--

DROP TABLE IF EXISTS `Matches`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Matches` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `WinnerID` int(11) NOT NULL,
  `Mom` int(11) DEFAULT NULL,
  `Feild_Umpire1` varchar(80) COLLATE utf8mb4_unicode_ci NOT NULL,
  `Feild_Umpire2` varchar(80) COLLATE utf8mb4_unicode_ci NOT NULL,
  `Stadium_name` varchar(150) COLLATE utf8mb4_unicode_ci NOT NULL,
  `Stadium_city` varchar(40) COLLATE utf8mb4_unicode_ci NOT NULL,
  `Season` int(11) DEFAULT NULL,
  PRIMARY KEY (`ID`),
  KEY `Winner_team` (`WinnerID`),
  KEY `mom_constraint` (`Mom`),
  KEY `Stadium_name` (`Stadium_name`,`Stadium_city`),
  CONSTRAINT `Winner_team` FOREIGN KEY (`WinnerID`) REFERENCES `Teams` (`TeamID`),
  CONSTRAINT `matches_ibfk_1` FOREIGN KEY (`Stadium_name`, `Stadium_city`) REFERENCES `Stadium` (`Stadium_Name`, `Stadium_City`),
  CONSTRAINT `mom_constraint` FOREIGN KEY (`Mom`) REFERENCES `Players` (`PlayerID`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Matches`
--

LOCK TABLES `Matches` WRITE;
/*!40000 ALTER TABLE `Matches` DISABLE KEYS */;
INSERT INTO `Matches` VALUES (4,3,18,'ump1','ump2','Sharjah','Dubai',2022);
/*!40000 ALTER TABLE `Matches` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `PlayerScorecard`
--

DROP TABLE IF EXISTS `PlayerScorecard`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `PlayerScorecard` (
  `MatchID` int(11) NOT NULL,
  `PlayerID` int(11) NOT NULL,
  `Wickets` int(11) DEFAULT 0,
  `Runs` int(11) DEFAULT 0,
  PRIMARY KEY (`MatchID`,`PlayerID`),
  KEY `PlayerID` (`PlayerID`),
  CONSTRAINT `playerscorecard_ibfk_1` FOREIGN KEY (`MatchID`) REFERENCES `Matches` (`ID`),
  CONSTRAINT `playerscorecard_ibfk_2` FOREIGN KEY (`PlayerID`) REFERENCES `Players` (`PlayerID`),
  CONSTRAINT `RunsNonNeg` CHECK (`Runs` >= 0),
  CONSTRAINT `WicketNonNeg` CHECK (`Wickets` >= 0)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `PlayerScorecard`
--

LOCK TABLES `PlayerScorecard` WRITE;
/*!40000 ALTER TABLE `PlayerScorecard` DISABLE KEYS */;
INSERT INTO `PlayerScorecard` VALUES (4,8,2,2),(4,9,3,3),(4,10,2,2),(4,11,2,2),(4,12,2,2),(4,14,3,3),(4,15,3,3),(4,16,3,3),(4,17,3,3),(4,18,3,3),(4,19,3,3),(4,20,3,3),(4,21,3,3),(4,22,3,3),(4,23,3,3),(4,24,2,2),(4,25,2,2),(4,26,2,2),(4,27,2,2),(4,28,2,2),(4,29,2,2),(4,30,2,2);
/*!40000 ALTER TABLE `PlayerScorecard` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Players`
--

DROP TABLE IF EXISTS `Players`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Players` (
  `Name` varchar(80) COLLATE utf8mb4_unicode_ci NOT NULL,
  `Age` int(11) DEFAULT NULL,
  `MoM` int(11) DEFAULT 0,
  `MatchesPlayed` int(11) DEFAULT 0,
  `PlayerID` int(11) NOT NULL AUTO_INCREMENT,
  `TeamID` int(11) DEFAULT NULL,
  PRIMARY KEY (`PlayerID`),
  KEY `TeamID` (`TeamID`),
  CONSTRAINT `Players_ibfk_1` FOREIGN KEY (`TeamID`) REFERENCES `Teams` (`TeamID`),
  CONSTRAINT `Age_positive` CHECK (`Age` >= 0)
) ENGINE=InnoDB AUTO_INCREMENT=32 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Players`
--

LOCK TABLES `Players` WRITE;
/*!40000 ALTER TABLE `Players` DISABLE KEYS */;
INSERT INTO `Players` VALUES ('dc4',23,0,1,8,4),('Chakka',34,0,1,9,3),('Bhai',69,0,1,10,4),('Add ',76,0,1,11,4),('addcheck',987,0,1,12,4),('hello',45,0,1,14,3),('srh1',23,0,1,15,3),('srh2',23,0,1,16,3),('srh5',24,0,1,17,3),('srh6',25,1,1,18,3),('srh7',26,0,1,19,3),('srh8',27,0,1,20,3),('srh9',11,0,1,21,3),('srh10',678,0,1,22,3),('srh11',23,0,1,23,3),('dc5',23,0,1,24,4),('dc6',23,0,1,25,4),('dc7',23,0,1,26,4),('dc8',23,0,1,27,4),('dc9',23,0,1,28,4),('dc10',23,0,1,29,4),('dc11',23,0,1,30,4);
/*!40000 ALTER TABLE `Players` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Plays`
--

DROP TABLE IF EXISTS `Plays`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Plays` (
  `Team_ID` int(11) DEFAULT NULL,
  `Season_Year` int(11) DEFAULT NULL,
  `Match_ID` int(11) DEFAULT NULL,
  `Stadium_name` varchar(150) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `Stadium_city` varchar(40) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  KEY `team_id_foreign` (`Team_ID`),
  KEY `match_id_foreign` (`Match_ID`),
  KEY `Stadium_name` (`Stadium_name`,`Stadium_city`),
  KEY `Season_Year` (`Season_Year`),
  CONSTRAINT `Plays_ibfk_1` FOREIGN KEY (`Stadium_name`, `Stadium_city`) REFERENCES `Stadium` (`Stadium_Name`, `Stadium_City`),
  CONSTRAINT `Plays_ibfk_2` FOREIGN KEY (`Season_Year`) REFERENCES `Seasons` (`Year`),
  CONSTRAINT `match_id_foreign` FOREIGN KEY (`Match_ID`) REFERENCES `Matches` (`ID`),
  CONSTRAINT `team_id_foreign` FOREIGN KEY (`Team_ID`) REFERENCES `Teams` (`TeamID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Plays`
--

LOCK TABLES `Plays` WRITE;
/*!40000 ALTER TABLE `Plays` DISABLE KEYS */;
INSERT INTO `Plays` VALUES (3,2022,4,'Sharjah','Dubai'),(4,2022,4,'Sharjah','Dubai');
/*!40000 ALTER TABLE `Plays` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Scorecard`
--

DROP TABLE IF EXISTS `Scorecard`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Scorecard` (
  `MatchID` int(11) DEFAULT NULL,
  `Team1` int(11) DEFAULT NULL,
  `Team2` int(11) DEFAULT NULL,
  KEY `MatchID` (`MatchID`),
  CONSTRAINT `Scorecard_ibfk_1` FOREIGN KEY (`MatchID`) REFERENCES `Matches` (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Scorecard`
--

LOCK TABLES `Scorecard` WRITE;
/*!40000 ALTER TABLE `Scorecard` DISABLE KEYS */;
INSERT INTO `Scorecard` VALUES (4,3,4);
/*!40000 ALTER TABLE `Scorecard` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Seasons`
--

DROP TABLE IF EXISTS `Seasons`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Seasons` (
  `Year` int(11) NOT NULL,
  `Finished` tinyint(1) DEFAULT 0,
  `PurpleCap` int(11) DEFAULT NULL,
  `OrangeCap` int(11) DEFAULT NULL,
  PRIMARY KEY (`Year`),
  KEY `PurpleCap` (`PurpleCap`),
  KEY `OrangeCap` (`OrangeCap`),
  CONSTRAINT `seasons_ibfk_1` FOREIGN KEY (`PurpleCap`) REFERENCES `Players` (`PlayerID`),
  CONSTRAINT `seasons_ibfk_2` FOREIGN KEY (`OrangeCap`) REFERENCES `Players` (`PlayerID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Seasons`
--

LOCK TABLES `Seasons` WRITE;
/*!40000 ALTER TABLE `Seasons` DISABLE KEYS */;
INSERT INTO `Seasons` VALUES (2019,1,NULL,NULL),(2022,1,14,9),(2026,1,NULL,NULL);
/*!40000 ALTER TABLE `Seasons` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Stadium`
--

DROP TABLE IF EXISTS `Stadium`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Stadium` (
  `Stadium_Name` varchar(150) COLLATE utf8mb4_unicode_ci NOT NULL,
  `Stadium_City` varchar(40) COLLATE utf8mb4_unicode_ci NOT NULL,
  `Max_capacity` int(11) NOT NULL,
  `Home_Team` int(11) NOT NULL,
  PRIMARY KEY (`Stadium_Name`,`Stadium_City`),
  KEY `home_team_fk` (`Home_Team`),
  CONSTRAINT `home_team_fk` FOREIGN KEY (`Home_Team`) REFERENCES `Teams` (`TeamID`),
  CONSTRAINT `capacity_positive` CHECK (`Max_capacity` > 0)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Stadium`
--

LOCK TABLES `Stadium` WRITE;
/*!40000 ALTER TABLE `Stadium` DISABLE KEYS */;
INSERT INTO `Stadium` VALUES ('notchinnaswamy','chennai',69420,5),('Rajiv Gandhi','Delhi',666,4),('Sharjah','Dubai',69420,3);
/*!40000 ALTER TABLE `Stadium` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `TeamManagement`
--

DROP TABLE IF EXISTS `TeamManagement`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `TeamManagement` (
  `TeamID` int(11) DEFAULT NULL,
  `Name` varchar(80) COLLATE utf8mb4_unicode_ci NOT NULL,
  `Role` varchar(80) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  KEY `TeamID` (`TeamID`),
  CONSTRAINT `TeamManagement_ibfk_1` FOREIGN KEY (`TeamID`) REFERENCES `Teams` (`TeamID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `TeamManagement`
--

LOCK TABLES `TeamManagement` WRITE;
/*!40000 ALTER TABLE `TeamManagement` DISABLE KEYS */;
INSERT INTO `TeamManagement` VALUES (3,'Phsyio','Physio');
/*!40000 ALTER TABLE `TeamManagement` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `TeamResults`
--

DROP TABLE IF EXISTS `TeamResults`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `TeamResults` (
  `SeasonYear` int(11) DEFAULT NULL,
  `TeamID` int(11) DEFAULT NULL,
  `Points` int(11) DEFAULT 0,
  KEY `SeasonYear` (`SeasonYear`),
  KEY `TeamID` (`TeamID`),
  CONSTRAINT `TeamResults_ibfk_1` FOREIGN KEY (`SeasonYear`) REFERENCES `Seasons` (`Year`),
  CONSTRAINT `TeamResults_ibfk_2` FOREIGN KEY (`TeamID`) REFERENCES `Teams` (`TeamID`),
  CONSTRAINT `PointsNonNeg` CHECK (`Points` >= 0)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `TeamResults`
--

LOCK TABLES `TeamResults` WRITE;
/*!40000 ALTER TABLE `TeamResults` DISABLE KEYS */;
INSERT INTO `TeamResults` VALUES (2022,3,2),(2022,4,0);
/*!40000 ALTER TABLE `TeamResults` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `TeamStandings`
--

DROP TABLE IF EXISTS `TeamStandings`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `TeamStandings` (
  `TeamID` int(11) DEFAULT NULL,
  `SeasonYear` int(11) DEFAULT NULL,
  `Standing` int(11) DEFAULT NULL,
  KEY `TeamID` (`TeamID`),
  KEY `SeasonYear` (`SeasonYear`),
  CONSTRAINT `TeamStandings_ibfk_1` FOREIGN KEY (`TeamID`) REFERENCES `Teams` (`TeamID`),
  CONSTRAINT `TeamStandings_ibfk_2` FOREIGN KEY (`SeasonYear`) REFERENCES `Seasons` (`Year`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `TeamStandings`
--

LOCK TABLES `TeamStandings` WRITE;
/*!40000 ALTER TABLE `TeamStandings` DISABLE KEYS */;
INSERT INTO `TeamStandings` VALUES (4,2022,1),(3,2022,2);
/*!40000 ALTER TABLE `TeamStandings` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Teams`
--

DROP TABLE IF EXISTS `Teams`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Teams` (
  `TeamID` int(11) NOT NULL AUTO_INCREMENT,
  `Name` varchar(80) COLLATE utf8mb4_unicode_ci NOT NULL,
  `CaptainID` int(11) DEFAULT NULL,
  PRIMARY KEY (`TeamID`),
  KEY `CaptainID` (`CaptainID`),
  CONSTRAINT `Teams_ibfk_1` FOREIGN KEY (`CaptainID`) REFERENCES `Players` (`PlayerID`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Teams`
--

LOCK TABLES `Teams` WRITE;
/*!40000 ALTER TABLE `Teams` DISABLE KEYS */;
INSERT INTO `Teams` VALUES (3,'SRH',9),(4,'DC',10),(5,'2',NULL),(6,'checkteam',NULL),(7,'hyd',NULL),(8,'lastcheck',NULL);
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

-- Dump completed on 2020-10-08 21:05:10
