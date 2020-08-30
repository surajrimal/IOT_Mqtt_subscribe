-- phpMyAdmin SQL Dump
-- version 4.8.5
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Dec 10, 2019 at 10:45 AM
-- Server version: 10.1.39-MariaDB
-- PHP Version: 7.2.18

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `nodem`
--

-- --------------------------------------------------------

--
-- Table structure for table `admin`
--

CREATE TABLE `admin` (
  `id` int(11) NOT NULL,
  `username` varchar(50) DEFAULT NULL,
  `password` varchar(64) DEFAULT NULL,
  `name` varchar(50) DEFAULT NULL,
  `email` varchar(70) DEFAULT NULL,
  `contact` varchar(14) DEFAULT NULL,
  `cDate` varchar(25) DEFAULT NULL,
  `status` varchar(10) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `admin`
--

INSERT INTO `admin` (`id`, `username`, `password`, `name`, `email`, `contact`, `cDate`, `status`) VALUES
(1, 'admin', '8c6976e5b5410415bde908bd4dee15dfb167a9c873fc4bb8a81f6f2ab448a918', 'Smart Insights', NULL, NULL, '1571907300', 'active');

-- --------------------------------------------------------

--
-- Table structure for table `dataontemp`
--

CREATE TABLE `dataontemp` (
  `id` int(11) NOT NULL,
  `deviceId` int(11) DEFAULT NULL,
  `temp` varchar(4) DEFAULT NULL,
  `humidity` varchar(4) DEFAULT NULL,
  `cDate` varchar(25) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `dataontemp`
--

INSERT INTO `dataontemp` (`id`, `deviceId`, `temp`, `humidity`, `cDate`) VALUES
(1, 1, '25', '76', '1571907300'),
(2, 1, '27', '76', '1571907300'),
(3, 1, '26', '76', '1571907300');

-- --------------------------------------------------------

--
-- Table structure for table `iotdevice`
--

CREATE TABLE `iotdevice` (
  `id` int(11) NOT NULL,
  `macAddress` varchar(25) DEFAULT NULL,
  `cDate` varchar(25) DEFAULT NULL,
  `status` varchar(10) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `iotdevice`
--

INSERT INTO `iotdevice` (`id`, `macAddress`, `cDate`, `status`) VALUES
(1, '123B6A1B6707', '1571907300', 'active'),
(2, '123B6A1B6708', '1571907300', 'disable');

-- --------------------------------------------------------

--
-- Table structure for table `temptrigger`
--

CREATE TABLE `temptrigger` (
  `id` int(11) NOT NULL,
  `deviceId` int(11) DEFAULT NULL,
  `point` varchar(4) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `temptrigger`
--

INSERT INTO `temptrigger` (`id`, `deviceId`, `point`) VALUES
(1, 1, '27');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `admin`
--
ALTER TABLE `admin`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `dataontemp`
--
ALTER TABLE `dataontemp`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `iotdevice`
--
ALTER TABLE `iotdevice`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `temptrigger`
--
ALTER TABLE `temptrigger`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `admin`
--
ALTER TABLE `admin`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `dataontemp`
--
ALTER TABLE `dataontemp`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `iotdevice`
--
ALTER TABLE `iotdevice`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `temptrigger`
--
ALTER TABLE `temptrigger`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
