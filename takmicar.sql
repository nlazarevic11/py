-- phpMyAdmin SQL Dump
-- version 5.0.3
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jan 27, 2022 at 07:49 PM
-- Server version: 10.4.14-MariaDB
-- PHP Version: 7.2.34

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `ispit2022`
--

-- --------------------------------------------------------

--
-- Table structure for table `takmicar`
--

CREATE TABLE `takmicar` (
  `id` int(11) NOT NULL,
  `broj_prijave` varchar(15) NOT NULL,
  `ime_prezime` varchar(50) NOT NULL,
  `email` varchar(50) NOT NULL,
  `sifra` varchar(50) NOT NULL,
  `matematika` int(11) NOT NULL,
  `programiranje` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `takmicar`
--

INSERT INTO `takmicar` (`id`, `broj_prijave`, `ime_prezime`, `email`, `sifra`, `matematika`, `programiranje`) VALUES
(1, '10-22', 'dusan sijacic', 'dsijacic@raf.rs', '123', 100, 50),
(2, '23-22', 'pera peric', 'pperic@raf.rs', '123', 90, 80),
(3, 'q15-22', 'dusan sijacic', 'dsijacic@raf.rs', '123', 80, 100);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `takmicar`
--
ALTER TABLE `takmicar`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `takmicar`
--
ALTER TABLE `takmicar`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
