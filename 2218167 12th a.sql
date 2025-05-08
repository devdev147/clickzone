-- MariaDB dump 10.19  Distrib 10.4.21-MariaDB, for Win64 (AMD64)
--
-- Host: localhost    Database: d2214167
-- ------------------------------------------------------
-- Server version	10.4.21-MariaDB

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
-- Table structure for table `app`
--

DROP TABLE IF EXISTS `app`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `app` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `folio` varchar(30) DEFAULT NULL,
  `name` varchar(30) DEFAULT NULL,
  `classsection` varchar(3) DEFAULT NULL,
  `ip` int(11) DEFAULT NULL,
  `phy` int(11) DEFAULT NULL,
  `maths` int(11) DEFAULT NULL,
  `acc` int(11) DEFAULT NULL,
  `bio` int(11) DEFAULT NULL,
  `eco` int(11) DEFAULT NULL,
  `chem` int(11) DEFAULT NULL,
  `bst` int(11) DEFAULT NULL,
  `eng` int(11) DEFAULT NULL,
  `remark` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `folio` (`folio`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `app`
--

LOCK TABLES `app` WRITE;
/*!40000 ALTER TABLE `app` DISABLE KEYS */;
INSERT INTO `app` VALUES (1,'228999','puneet','11A',90,91,92,NULL,93,NULL,94,NULL,95,'above average'),(2,'222456','yogesh','11A',70,59,89,NULL,78,NULL,67,NULL,95,'average'),(3,'221154','himanshu','11A',75,79,89,NULL,78,NULL,67,NULL,95,'below average'),(4,'221134','rakesh','11C',95,NULL,NULL,75,NULL,85,NULL,95,95,'good'),(5,'221145','pushpa','11C',90,NULL,NULL,84,NULL,87,NULL,90,95,'bad'),(7,'696969','PRANTAP','11A',94,30,92,NULL,90,NULL,88,NULL,82,'PHY!!'),(8,'2184317','PUNEET K','11A',79,84,64,NULL,94,NULL,96,NULL,74,'AVERAGE'),(9,'2214044','BABLU PICASOO','11C',96,NULL,NULL,88,NULL,74,NULL,94,82,'G'),(10,'2214184','RAKESH','11A',92,88,78,NULL,88,NULL,99,NULL,70,'G'),(11,'2184042','YOGESH TIWARI','11A',99,98,100,NULL,102,NULL,99,NULL,103,'EXCEELENT');
/*!40000 ALTER TABLE `app` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `app1`
--

DROP TABLE IF EXISTS `app1`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `app1` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `folio` int(11) DEFAULT NULL,
  `name` varchar(30) DEFAULT NULL,
  `classsection` varchar(3) DEFAULT NULL,
  `ip` int(11) DEFAULT NULL,
  `phy` int(11) DEFAULT NULL,
  `maths` int(11) DEFAULT NULL,
  `acc` int(11) DEFAULT NULL,
  `bio` int(11) DEFAULT NULL,
  `eco` int(11) DEFAULT NULL,
  `chem` int(11) DEFAULT NULL,
  `bst` int(11) DEFAULT NULL,
  `eng` int(11) DEFAULT NULL,
  `remark` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `folio` (`folio`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `app1`
--

LOCK TABLES `app1` WRITE;
/*!40000 ALTER TABLE `app1` DISABLE KEYS */;
/*!40000 ALTER TABLE `app1` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `application1`
--

DROP TABLE IF EXISTS `application1`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `application1` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `folio` int(11) DEFAULT NULL,
  `name` varchar(30) DEFAULT NULL,
  `classsection` varchar(3) DEFAULT NULL,
  `marks1` int(11) DEFAULT NULL,
  `marks2` int(11) DEFAULT NULL,
  `marks3` int(11) DEFAULT NULL,
  `remark` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `folio` (`folio`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `application1`
--

LOCK TABLES `application1` WRITE;
/*!40000 ALTER TABLE `application1` DISABLE KEYS */;
/*!40000 ALTER TABLE `application1` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `company_name`
--

DROP TABLE IF EXISTS `company_name`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `company_name` (
  `company_name_id` int(11) NOT NULL AUTO_INCREMENT,
  `company_name` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`company_name_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `company_name`
--

LOCK TABLES `company_name` WRITE;
/*!40000 ALTER TABLE `company_name` DISABLE KEYS */;
INSERT INTO `company_name` VALUES (1,'CLICK ZONE');
/*!40000 ALTER TABLE `company_name` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `companyname`
--

DROP TABLE IF EXISTS `companyname`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `companyname` (
  `companyname_id` int(11) NOT NULL AUTO_INCREMENT,
  `company_name` varchar(30) DEFAULT NULL,
  `gst_invoice` int(11) DEFAULT NULL,
  PRIMARY KEY (`companyname_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `companyname`
--

LOCK TABLES `companyname` WRITE;
/*!40000 ALTER TABLE `companyname` DISABLE KEYS */;
/*!40000 ALTER TABLE `companyname` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `coustomer`
--

DROP TABLE IF EXISTS `coustomer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `coustomer` (
  `coustomer_id` int(11) NOT NULL AUTO_INCREMENT,
  `coustomer_name` varchar(30) DEFAULT NULL,
  `coustomer_city` varchar(30) DEFAULT NULL,
  `coustomer_country` varchar(30) DEFAULT NULL,
  `coustomer_email` varchar(30) DEFAULT NULL,
  `coustomer_mobile` char(10) DEFAULT NULL,
  `coustomer_category` varchar(10) DEFAULT NULL,
  `coustomer_rating` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`coustomer_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `coustomer`
--

LOCK TABLES `coustomer` WRITE;
/*!40000 ALTER TABLE `coustomer` DISABLE KEYS */;
INSERT INTO `coustomer` VALUES (1,'Devyansh','delhi','india','deopadev@gmail.com','9897282762','for person','average'),(2,'moih','tas','fgghi','dhd@gmail.com','568686474','profession','good');
/*!40000 ALTER TABLE `coustomer` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `customer`
--

DROP TABLE IF EXISTS `customer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `customer` (
  `customerid` int(11) NOT NULL AUTO_INCREMENT,
  `customercode` varchar(30) DEFAULT NULL,
  `customername` varchar(30) DEFAULT NULL,
  `customermobile` varchar(10) DEFAULT NULL,
  `customercategory` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`customerid`),
  UNIQUE KEY `customercode` (`customercode`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `customer`
--

LOCK TABLES `customer` WRITE;
/*!40000 ALTER TABLE `customer` DISABLE KEYS */;
INSERT INTO `customer` VALUES (1,'1','Customer01','9411107750','Gold'),(2,'2','Customer02','9817612569','Gold'),(3,'3','Customer03','7891235490','Silver'),(4,'4','Customer04','9412189011','Gold'),(5,'5','Customer05','9413189022','Platinum');
/*!40000 ALTER TABLE `customer` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `customercategory`
--

DROP TABLE IF EXISTS `customercategory`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `customercategory` (
  `customercategoryid` int(11) NOT NULL AUTO_INCREMENT,
  `customercategory` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`customercategoryid`),
  UNIQUE KEY `customercategory` (`customercategory`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `customercategory`
--

LOCK TABLES `customercategory` WRITE;
/*!40000 ALTER TABLE `customercategory` DISABLE KEYS */;
INSERT INTO `customercategory` VALUES (1,'Gold'),(3,'Platinum'),(2,'Silver');
/*!40000 ALTER TABLE `customercategory` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ipl1`
--

DROP TABLE IF EXISTS `ipl1`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `ipl1` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `playerid` varchar(30) DEFAULT NULL,
  `name` varchar(30) DEFAULT NULL,
  `team` varchar(30) DEFAULT NULL,
  `highestrun` int(11) DEFAULT NULL,
  `lowestrun` int(11) DEFAULT NULL,
  `bowlplayed` int(11) DEFAULT NULL,
  `totalrun` int(11) DEFAULT NULL,
  `wicket` int(11) DEFAULT NULL,
  `matchplayed` int(11) DEFAULT NULL,
  `remark` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `playerid` (`playerid`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ipl1`
--

LOCK TABLES `ipl1` WRITE;
/*!40000 ALTER TABLE `ipl1` DISABLE KEYS */;
INSERT INTO `ipl1` VALUES (1,'10','puneet','csk',102,0,156,760,7,9,'a young great player'),(2,'1','yogesh','lsg',79,0,132,402,6,8,'good player'),(3,'2','rakesh','dc',99,1,111,630,9,11,'great'),(4,'3','amit','lsg',69,69,40,69,0,1,'new player'),(5,'69','bablu','gt',154,0,550,7000,78,170,'excellent'),(6,'fh','fdghu','hudf',8,9,98,989,89,98,'98');
/*!40000 ALTER TABLE `ipl1` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `item`
--

DROP TABLE IF EXISTS `item`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `item` (
  `itemid` int(11) NOT NULL AUTO_INCREMENT,
  `itemcode` int(11) DEFAULT NULL,
  `itemname` varchar(30) DEFAULT NULL,
  `itemunit` varchar(30) DEFAULT NULL,
  `itemcategory` varchar(30) DEFAULT NULL,
  `itemgstrate` decimal(5,2) DEFAULT NULL,
  `itemtotalstock` decimal(10,2) DEFAULT 0.00,
  `itemaverageprice` decimal(10,2) DEFAULT 0.00,
  PRIMARY KEY (`itemid`),
  UNIQUE KEY `itemcode` (`itemcode`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `item`
--

LOCK TABLES `item` WRITE;
/*!40000 ALTER TABLE `item` DISABLE KEYS */;
INSERT INTO `item` VALUES (1,1,'sugar','Kg','IC1',12.00,5.00,100.00),(2,2,'Item02','Kg','IC1',12.00,2.00,150.00),(3,3,'Item03','No','IC1',12.00,3.00,30.00),(4,4,'Item04','Pkt','IC2',12.00,4.00,450.00),(5,5,'Item05','No','IC3',12.00,1.00,25.00);
/*!40000 ALTER TABLE `item` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `itemcategory`
--

DROP TABLE IF EXISTS `itemcategory`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `itemcategory` (
  `itemcategoryid` int(11) NOT NULL AUTO_INCREMENT,
  `itemcategory` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`itemcategoryid`),
  UNIQUE KEY `itemcategory` (`itemcategory`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `itemcategory`
--

LOCK TABLES `itemcategory` WRITE;
/*!40000 ALTER TABLE `itemcategory` DISABLE KEYS */;
INSERT INTO `itemcategory` VALUES (1,'IC1'),(2,'IC2'),(3,'IC3');
/*!40000 ALTER TABLE `itemcategory` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `itempurchase`
--

DROP TABLE IF EXISTS `itempurchase`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `itempurchase` (
  `itempurchaseid` int(11) NOT NULL AUTO_INCREMENT,
  `pdate` date DEFAULT NULL,
  `invoice` varchar(30) DEFAULT NULL,
  `suppliercategory` varchar(30) DEFAULT NULL,
  `suppliercode` varchar(30) DEFAULT NULL,
  `suppliername` varchar(30) DEFAULT NULL,
  `suppliermobile` varchar(30) DEFAULT NULL,
  `itemcode` varchar(30) DEFAULT NULL,
  `itemcategory` varchar(30) DEFAULT NULL,
  `itemname` varchar(30) DEFAULT NULL,
  `itemunit` varchar(30) DEFAULT NULL,
  `itemgstrate` decimal(5,2) DEFAULT NULL,
  `itemquantity` decimal(10,2) DEFAULT NULL,
  `itemstock` decimal(10,2) DEFAULT NULL,
  `itemprice` decimal(10,2) DEFAULT NULL,
  `amount` decimal(10,2) DEFAULT NULL,
  `fright` decimal(10,2) DEFAULT NULL,
  `gst` decimal(10,2) DEFAULT NULL,
  `netamount` decimal(10,2) DEFAULT NULL,
  `grandamount` decimal(10,2) DEFAULT NULL,
  `itemminsaleprice` decimal(10,2) DEFAULT NULL,
  PRIMARY KEY (`itempurchaseid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `itempurchase`
--

LOCK TABLES `itempurchase` WRITE;
/*!40000 ALTER TABLE `itempurchase` DISABLE KEYS */;
/*!40000 ALTER TABLE `itempurchase` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `itemsale`
--

DROP TABLE IF EXISTS `itemsale`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `itemsale` (
  `itemsaleid` int(11) NOT NULL AUTO_INCREMENT,
  `sdate` date DEFAULT NULL,
  `invoice` varchar(30) DEFAULT NULL,
  `customercategory` varchar(30) DEFAULT NULL,
  `customercode` varchar(30) DEFAULT NULL,
  `customername` varchar(30) DEFAULT NULL,
  `customermobile` varchar(30) DEFAULT NULL,
  `itemcode` varchar(30) DEFAULT NULL,
  `itemname` varchar(30) DEFAULT NULL,
  `itemcategory` varchar(30) DEFAULT NULL,
  `itemunit` varchar(30) DEFAULT NULL,
  `itemgstrate` decimal(5,2) DEFAULT NULL,
  `itemquantity` decimal(10,2) DEFAULT NULL,
  `itemprice` decimal(10,2) DEFAULT NULL,
  `amount` decimal(10,2) DEFAULT NULL,
  `marginpercent` decimal(10,2) DEFAULT NULL,
  `gst` decimal(10,2) DEFAULT NULL,
  `netamount` decimal(10,2) DEFAULT NULL,
  `fright` decimal(10,2) DEFAULT NULL,
  `grandamount` decimal(10,2) DEFAULT NULL,
  PRIMARY KEY (`itemsaleid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `itemsale`
--

LOCK TABLES `itemsale` WRITE;
/*!40000 ALTER TABLE `itemsale` DISABLE KEYS */;
/*!40000 ALTER TABLE `itemsale` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `itemunit`
--

DROP TABLE IF EXISTS `itemunit`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `itemunit` (
  `itemunitid` int(11) NOT NULL AUTO_INCREMENT,
  `itemunit` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`itemunitid`),
  UNIQUE KEY `itemunit` (`itemunit`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `itemunit`
--

LOCK TABLES `itemunit` WRITE;
/*!40000 ALTER TABLE `itemunit` DISABLE KEYS */;
INSERT INTO `itemunit` VALUES (2,'cm'),(4,'dz'),(1,'Kg'),(3,'lt'),(5,'No.');
/*!40000 ALTER TABLE `itemunit` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `netflix`
--

DROP TABLE IF EXISTS `netflix`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `netflix` (
  `title` varchar(30) DEFAULT NULL,
  `director` varchar(30) DEFAULT NULL,
  `cast` varchar(30) DEFAULT NULL,
  `country` varchar(30) DEFAULT NULL,
  `rating` varchar(30) DEFAULT NULL,
  `release_year` varchar(30) DEFAULT NULL,
  `duration` varchar(30) DEFAULT NULL,
  `about` varchar(300) DEFAULT NULL,
  `pic` varchar(30) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `netflix`
--

LOCK TABLES `netflix` WRITE;
/*!40000 ALTER TABLE `netflix` DISABLE KEYS */;
/*!40000 ALTER TABLE `netflix` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `person`
--

DROP TABLE IF EXISTS `person`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `person` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(30) DEFAULT NULL,
  `name` varchar(30) DEFAULT NULL,
  `gender` varchar(30) DEFAULT NULL,
  `hobby` varchar(300) DEFAULT NULL,
  `pic` varchar(30) DEFAULT NULL,
  `dob` date DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `person`
--

LOCK TABLES `person` WRITE;
/*!40000 ALTER TABLE `person` DISABLE KEYS */;
INSERT INTO `person` VALUES (9,'Mr.','Xyz','M','Reading,Writing','1.png','2022-09-07'),(10,'Ms.','abcd','F','Reading,Writing,Swimming','2.png','2012-03-15'),(11,'Mr.','dev','M','Reading,Writing','muph084-b001-f090-sl001-i029-0','2006-05-12'),(12,'Mr.','dev','M','sleeping','The-World-of-Robots-What-Does-','2005-04-07'),(13,'Mr.','tyjkyh','M','Reading,Writing,Swimming','3.jpg','2023-08-23');
/*!40000 ALTER TABLE `person` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `place`
--

DROP TABLE IF EXISTS `place`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `place` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `placename` varchar(50) DEFAULT NULL,
  `wheresituated` varchar(100) DEFAULT NULL,
  `weather` varchar(100) DEFAULT NULL,
  `peoplevisiting` varchar(200) DEFAULT NULL,
  `besttimetovisit` varchar(100) DEFAULT NULL,
  `about` longtext DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `placename` (`placename`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `place`
--

LOCK TABLES `place` WRITE;
/*!40000 ALTER TABLE `place` DISABLE KEYS */;
INSERT INTO `place` VALUES (1,'french quarter','New Orleans , Louisiana','humid, subtropical','825,000 packed New Orleans for French\n                Quarter Fest 2022','February to May','The French Quarter is the city historic heart, famous for\n                its vibrant nightlife and colorful buildings with cast-iron balconies. Crowd-pleasing Bourbon\n                Street features jazz clubs, Cajun eateries and raucous bars serving potent cocktails.\n                Quieter streets lead to the French Market, with gourmet food and local crafts, and to\n                Jackson Square where street performers entertain in front of soaring St. Louis Cathedral.'),(2,'zurich','switzerland','Zurich lies in the temperate climate zone and has four distinct seasons. In\n                winter, ','the country recorded a whopping 12 million tourist visits in 2019.','June to August','The city of Zurich, a global center for banking and finance, lies at the north end of Lake Zurich in\n                northern Switzerland. The picturesque lanes of the central Altstadt (Old Town), on either side of the\n                Limmat River, reflect its pre-medieval history. Waterfront promenades like the Limmatquai follow\n                the river toward the 17th-century Rathaus (town hall).'),(3,'paris','france','mostly mild weather','over 44 million visitors','February to April','Paris, France\n                capital, is a major European city and a global center for art, fashion, gastronomy and culture. Its 19th-century\n                cityscape is crisscrossed by wide boulevards and the River Seine. Beyond such landmarks as the Eiffel Tower and\n                the 12th-century, Gothic Notre-Dame cathedral, the city is known for its cafe culture and designer boutiques\n                along the Rue du Faubourg Saint-Honoré.'),(5,'malta','europe','Summer is hot and dry with temperatures reaching 32 °C in July and August. Winter is mild and wet, a','2.3 million people per year','june to october','Malta is an archipelago in the central Mediterranean between Sicily and the North African coast. It is a nation known for historic sites related to a succession of rulers including the Romans, Moors, Knights of Saint John, French and British. It has numerous fortresses, megalithic temples and the Ħal Saflieni Hypogeum, a subterranean complex of halls and burial chambers dating to circa 4000 B.C'),(6,'goa','india','Goa enjoys a tropical monsoon climate under the Koppen climate classification that features a pleasa',' 33.08 lakh domestic and 0.22 lakh foreign tourists ','november to february','Goa is a state in western India with coastlines stretching along the Arabian Sea. Its long history as a Portuguese colony prior to 1961 is evident in its preserved 17th-century churches and the area’s tropical spice plantations. Goa is also known for its beaches, ranging from   popular stretches at Baga and Palolem to those in laid-back fishing villages such as Agonda'),(7,'giza','egypt ,africa','hot desert climate','about 14 million people per year','october to april','Giza is an Egyptian city on the west bank of the Nile, near Cairo. The Giza Plateau is home to iconic Egyptian monuments, including 3   tall pyramids built as royal mausoleums around the 26th century B.C. The largest, the Great Pyramid, is King Khufu’s tomb. The Great Sphinx is a vast sculpture of a man’s head on a lion’s body. The Solar Boat Museum displays a restored cedar barge found buried near the Great Pyramid.'),(8,'alaska','united state','from about 45 to 75 °F (7 to 24 °C) in summer and about 20 to −10 °F (−7 to −23 °C) in winter.','around 2.26 million','(september to march) between this time you can see northern lights','Alaska is a U.S. state on the northwest extremity of North America. A semi-exclave of the U.S., it borders British Columbia and Yukon   in Canada to the east, and it shares a western maritime border in the Bering Strait with the Russian Federation\'s Chukotka Autonomous Okrug. '),(9,'bangkok','thailand','Bangkok enjoys a tropical monsoon climate, meaning that it has 3 main  seasons: hot season from Marc','22.7 million international tourist','november to february','Bangkok, Thailand’s capital, is a large city known for ornate shrines and vibrant street life. The boat-filled Chao Phraya River feeds its network of canals, flowing past the Rattanakosin royal district, home to opulent Grand Palace and its sacred Wat Phra Kaew Temple. Nearby is Wat Pho Temple with an enormous reclining Buddha and, on the opposite shore, Wat Arun Temple with its steep steps and Khmer-style spire.');
/*!40000 ALTER TABLE `place` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `product`
--

DROP TABLE IF EXISTS `product`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `product` (
  `product_id` int(11) NOT NULL AUTO_INCREMENT,
  `product_name` varchar(30) DEFAULT NULL,
  `product_category` varchar(30) DEFAULT NULL,
  `product_unit` int(11) DEFAULT NULL,
  `product_features` varchar(100) DEFAULT NULL,
  `product_company` varchar(30) DEFAULT NULL,
  `warranty_period` varchar(30) DEFAULT NULL,
  `product_photo` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`product_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `product`
--

LOCK TABLES `product` WRITE;
/*!40000 ALTER TABLE `product` DISABLE KEYS */;
INSERT INTO `product` VALUES (1,'nikon d7000','dslr',10,'this camera is good for professional photographer for weddings and other occaison','nikon','4years','er.jpeg'),(2,'canon c6','dslr',1,'good for potrait','canon','2 years','dhdhd');
/*!40000 ALTER TABLE `product` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `product_category`
--

DROP TABLE IF EXISTS `product_category`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `product_category` (
  `product_category_id` int(11) NOT NULL AUTO_INCREMENT,
  `product_category` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`product_category_id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `product_category`
--

LOCK TABLES `product_category` WRITE;
/*!40000 ALTER TABLE `product_category` DISABLE KEYS */;
INSERT INTO `product_category` VALUES (1,'dslr'),(2,'slr'),(3,'movie camera'),(4,'tripod'),(5,'other accesories');
/*!40000 ALTER TABLE `product_category` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `purchase`
--

DROP TABLE IF EXISTS `purchase`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `purchase` (
  `purchase_id` int(11) NOT NULL AUTO_INCREMENT,
  `product_name` varchar(30) DEFAULT NULL,
  `supplier_id` int(11) DEFAULT NULL,
  `supplier_name` varchar(30) DEFAULT NULL,
  `supplier_city` varchar(30) DEFAULT NULL,
  `product_category` varchar(30) DEFAULT NULL,
  `product_unit` int(11) DEFAULT NULL,
  `netpurchaseprice` int(11) DEFAULT NULL,
  `transdate` date DEFAULT NULL,
  `gst` varchar(5) DEFAULT NULL,
  `totalamount` varchar(10) DEFAULT NULL,
  `price` varchar(10) DEFAULT NULL,
  `gstamount` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`purchase_id`),
  UNIQUE KEY `supplier_id` (`supplier_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `purchase`
--

LOCK TABLES `purchase` WRITE;
/*!40000 ALTER TABLE `purchase` DISABLE KEYS */;
INSERT INTO `purchase` VALUES (1,'d7000',1,'vivaan','delhi','dslr',100,9820,'2024-09-09','18%','9000','9000','1300');
/*!40000 ALTER TABLE `purchase` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `purchase_return`
--

DROP TABLE IF EXISTS `purchase_return`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `purchase_return` (
  `purchase_return_id` int(11) NOT NULL AUTO_INCREMENT,
  `net_amount` int(11) DEFAULT NULL,
  `product_name` varchar(30) DEFAULT NULL,
  `supplier_code` int(11) DEFAULT NULL,
  `supplier_name` varchar(30) DEFAULT NULL,
  `supplier_city` varchar(30) DEFAULT NULL,
  `product_category` varchar(30) DEFAULT NULL,
  `product_unit` int(11) DEFAULT NULL,
  `transdate` date DEFAULT NULL,
  `product_review` varchar(30) DEFAULT NULL,
  `supplier_review` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`purchase_return_id`),
  UNIQUE KEY `supplier_code` (`supplier_code`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `purchase_return`
--

LOCK TABLES `purchase_return` WRITE;
/*!40000 ALTER TABLE `purchase_return` DISABLE KEYS */;
/*!40000 ALTER TABLE `purchase_return` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `replacement_refund`
--

DROP TABLE IF EXISTS `replacement_refund`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `replacement_refund` (
  `replacement_refund_id` int(11) NOT NULL AUTO_INCREMENT,
  `product_code` varchar(30) DEFAULT NULL,
  `product_name` varchar(30) DEFAULT NULL,
  `coustomer_id` int(11) DEFAULT NULL,
  `coustomer_name` varchar(20) DEFAULT NULL,
  `product_category` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`replacement_refund_id`),
  UNIQUE KEY `product_code` (`product_code`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `replacement_refund`
--

LOCK TABLES `replacement_refund` WRITE;
/*!40000 ALTER TABLE `replacement_refund` DISABLE KEYS */;
INSERT INTO `replacement_refund` VALUES (1,'123','d7000',123,'shiv','dslr');
/*!40000 ALTER TABLE `replacement_refund` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sale`
--

DROP TABLE IF EXISTS `sale`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `sale` (
  `sale_id` int(11) NOT NULL AUTO_INCREMENT,
  `product_name` varchar(30) DEFAULT NULL,
  `coustomer_id` int(11) DEFAULT NULL,
  `coustomer_name` varchar(30) DEFAULT NULL,
  `product_category` varchar(30) DEFAULT NULL,
  `product_unit` int(11) DEFAULT NULL,
  `warranty_period` varchar(30) DEFAULT NULL,
  `transdate` date DEFAULT NULL,
  `sale_price` int(11) DEFAULT NULL,
  `gst` int(11) DEFAULT NULL,
  `total_amount` varchar(10) DEFAULT NULL,
  `gst_amount` varchar(10) DEFAULT NULL,
  `net_amount` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`sale_id`),
  UNIQUE KEY `coustomer_id` (`coustomer_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sale`
--

LOCK TABLES `sale` WRITE;
/*!40000 ALTER TABLE `sale` DISABLE KEYS */;
INSERT INTO `sale` VALUES (1,'d7000',10,'Devyansh','dslr',1,'3years','2024-09-09',10000,18,'10000','1800','11800');
/*!40000 ALTER TABLE `sale` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sale_return`
--

DROP TABLE IF EXISTS `sale_return`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `sale_return` (
  `sale_return_id` int(11) NOT NULL AUTO_INCREMENT,
  `netrefundamount` int(11) DEFAULT NULL,
  `product_name` varchar(30) DEFAULT NULL,
  `coustomer_code` int(11) DEFAULT NULL,
  `coustomer_name` varchar(30) DEFAULT NULL,
  `product_unit` int(11) DEFAULT NULL,
  `transdate` date DEFAULT NULL,
  `warranty_period` varchar(30) DEFAULT NULL,
  `under_warranty` varchar(3) DEFAULT NULL,
  `faultinitem` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`sale_return_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sale_return`
--

LOCK TABLES `sale_return` WRITE;
/*!40000 ALTER TABLE `sale_return` DISABLE KEYS */;
/*!40000 ALTER TABLE `sale_return` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `student`
--

DROP TABLE IF EXISTS `student`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `student` (
  `SN` int(11) NOT NULL,
  `NAME` varchar(30) DEFAULT NULL,
  `class` varchar(3) DEFAULT NULL,
  `GENDER` char(1) DEFAULT NULL,
  `dob` date DEFAULT NULL,
  `doj` date DEFAULT NULL,
  `fee` decimal(10,2) DEFAULT NULL,
  `marks` int(11) DEFAULT NULL,
  `grade` varchar(2) DEFAULT NULL,
  `result` varchar(30) DEFAULT NULL,
  `house` varchar(30) DEFAULT NULL,
  `city` varchar(30) DEFAULT NULL,
  `FinalPrice` decimal(10,1) DEFAULT NULL,
  PRIMARY KEY (`SN`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `student`
--

LOCK TABLES `student` WRITE;
/*!40000 ALTER TABLE `student` DISABLE KEYS */;
INSERT INTO `student` VALUES (1,'Devyansh','11A','M','2008-03-07','2018-04-13',500000.00,100,'B1','pass','nehru','tanakpur',560000.0),(2,'Gauransh','11A','M','2007-02-12','2018-04-04',54000.00,33,'D1','pass','nehru','puranpur',60480.0),(3,'SIT','11c','M','2001-03-02','2022-01-01',540000.00,99,'a1','pass','tagore','rajnagar',604800.0),(4,'sidhart','11c','M','2007-04-07','2021-04-04',117000.00,69,'B2','pass','pant','Delhi',131040.0),(5,'Shivansh','11c','M','2008-12-12','2021-04-07',501123.00,66,'B2','pass','nehru','Lucknow',561257.8),(6,'Ayush','11A','M','2006-03-25','2021-04-04',117000.00,88,'A2','pass','nehru','devipura',131040.0),(7,'Nishant','11A','M','2006-09-09','2022-09-09',450000.00,56,'B2','pass','tilak','lucknow',504000.0),(8,'Prajjwal','11A','M','2008-06-17','2023-03-04',54000.00,90,'A2','pass','nehru','lucknow',60480.0),(9,'Raj','11A','M','2008-09-12','2019-04-04',440000.00,99,'A1','pass','pant','bijor',492800.0),(10,'Saksham','11A','M','2006-12-09','2005-04-21',54000.00,45,'C1','pass','tagore','Delhi',60480.0),(11,'Prakhar','11A','M','2008-09-23','2018-04-01',54000.00,99,'A1','pass','pant','srinagar',60480.0);
/*!40000 ALTER TABLE `student` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `student1`
--

DROP TABLE IF EXISTS `student1`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `student1` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `folio` int(11) DEFAULT NULL,
  `name` varchar(30) DEFAULT NULL,
  `house` varchar(30) DEFAULT NULL,
  `classsection` varchar(3) DEFAULT NULL,
  `dob` date DEFAULT NULL,
  `marks` int(11) DEFAULT NULL,
  `fee` decimal(10,2) DEFAULT NULL,
  `remark` varchar(255) DEFAULT NULL,
  `photo` varchar(30) DEFAULT NULL,
  `gender` char(1) DEFAULT NULL,
  `cocurriculars` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `folio` (`folio`)
) ENGINE=InnoDB AUTO_INCREMENT=29 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `student1`
--

LOCK TABLES `student1` WRITE;
/*!40000 ALTER TABLE `student1` DISABLE KEYS */;
/*!40000 ALTER TABLE `student1` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `student3`
--

DROP TABLE IF EXISTS `student3`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `student3` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `roll_number` varchar(20) NOT NULL,
  `email` varchar(255) NOT NULL,
  `student_pic` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `student3`
--

LOCK TABLES `student3` WRITE;
/*!40000 ALTER TABLE `student3` DISABLE KEYS */;
/*!40000 ALTER TABLE `student3` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `students`
--

DROP TABLE IF EXISTS `students`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `students` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `roll_number` varchar(20) NOT NULL,
  `email` varchar(255) NOT NULL,
  `student_pic` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `students`
--

LOCK TABLES `students` WRITE;
/*!40000 ALTER TABLE `students` DISABLE KEYS */;
INSERT INTO `students` VALUES (1,'John Doe','2021001','johndoe@example.com','uploads/1.png'),(2,'Jane Smith','2021002','janesmith@example.com','uploads/2.png'),(3,'Michael Johnson','2021003','michael@example.com','uploads/3.png'),(4,'Emily Davis','2021004','emily@example.com','uploads/4.png'),(5,'David Wilson','2021005','david@example.com','uploads/5.png');
/*!40000 ALTER TABLE `students` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `supplier`
--

DROP TABLE IF EXISTS `supplier`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `supplier` (
  `supplier_id` int(11) NOT NULL AUTO_INCREMENT,
  `supplier_name` varchar(30) DEFAULT NULL,
  `supplier_country` varchar(30) DEFAULT NULL,
  `supplier_city` varchar(30) DEFAULT NULL,
  `supplier_company` varchar(30) DEFAULT NULL,
  `supplier_category` varchar(30) DEFAULT NULL,
  `supplier_contact` varchar(11) DEFAULT NULL,
  `supplier_rating` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`supplier_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `supplier`
--

LOCK TABLES `supplier` WRITE;
/*!40000 ALTER TABLE `supplier` DISABLE KEYS */;
INSERT INTO `supplier` VALUES (1,'sanju','India','delhi','nikon','wholeseller','9896754902','good');
/*!40000 ALTER TABLE `supplier` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `suppliercategory`
--

DROP TABLE IF EXISTS `suppliercategory`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `suppliercategory` (
  `suppliercategoryid` int(11) NOT NULL AUTO_INCREMENT,
  `suppliercategory` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`suppliercategoryid`),
  UNIQUE KEY `suppliercategory` (`suppliercategory`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `suppliercategory`
--

LOCK TABLES `suppliercategory` WRITE;
/*!40000 ALTER TABLE `suppliercategory` DISABLE KEYS */;
INSERT INTO `suppliercategory` VALUES (1,'SC1'),(2,'SC2'),(3,'SC3');
/*!40000 ALTER TABLE `suppliercategory` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `user` (
  `username` varchar(30) NOT NULL,
  `password` varchar(30) DEFAULT NULL,
  `userrole` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES ('admin','1234','admin'),('user1','1234','limited user'),('user2','1234','limited user');
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `users` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(50) NOT NULL,
  `password` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `phone` varchar(255) NOT NULL,
  `created_at` datetime DEFAULT current_timestamp(),
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1,'admin','abcd1234','admin@bvm.com','1234567890','2023-09-26 08:36:06'),(2,'dev123','$2y$10$d2R6743Cm.Ihl5OzgEvn1OZc7H3u1IX8VA7CspJ3UpZTaJlmo1lyW','','','2023-09-26 08:36:38');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-09-03 10:12:36
