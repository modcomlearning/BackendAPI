-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Dec 21, 2024 at 01:05 PM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.0.30

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `BackendAPI`
--

-- --------------------------------------------------------

--
-- Table structure for table `land_details`
--

CREATE TABLE `land_details` (
  `land_id` int(11) NOT NULL,
  `land_description` text DEFAULT NULL,
  `land_location` varchar(255) DEFAULT NULL,
  `land_cost` int(11) DEFAULT NULL,
  `land_size` varchar(50) DEFAULT NULL,
  `land_owner` varchar(255) DEFAULT NULL,
  `plot_no` varchar(50) DEFAULT NULL,
  `land_photo` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `land_details`
--

INSERT INTO `land_details` (`land_id`, `land_description`, `land_location`, `land_cost`, `land_size`, `land_owner`, `plot_no`, `land_photo`) VALUES
(1, 'A large agricultural plot with fertile soil, suitable for farming.', 'Dallas, Texas, USA', 750000, '20000 sq ft', 'Alice Johnson', 'TX9876', ''),
(2, 'A great farm for growing maize, very warm and fertile', 'Kahawa, Nairobi, Kenya', 750000, '70000 sq ft', 'John Dere', 'NB9876', ''),
(3, ' Nice Land', 'Mwiki', 100000, '2 Acres', 'Joseph', 'jhgjh526', 'airo.jpeg');

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `user_id` int(11) NOT NULL,
  `username` varchar(50) NOT NULL,
  `password` varchar(100) NOT NULL,
  `email` varchar(50) NOT NULL,
  `phone` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`user_id`, `username`, `password`, `email`, `phone`) VALUES
(1, 'Tom', '123456', 'tom@gmail.com', '0745131971'),
(2, 'tom', '54556465', 'tom@gmail.com', '0712121212');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `land_details`
--
ALTER TABLE `land_details`
  ADD PRIMARY KEY (`land_id`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`user_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `land_details`
--
ALTER TABLE `land_details`
  MODIFY `land_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `user_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
