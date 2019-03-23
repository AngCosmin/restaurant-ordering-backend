CREATE DATABASE app;
use app;

CREATE TABLE `users` (
  `id` int(11) NOT NULL,
  `username` varchar(30) DEFAULT NULL,
  `password` varchar(30) DEFAULT NULL
);

INSERT INTO `users` (`id`, `username`, `password`) VALUES (1, 'Cosmin', '123'), (2, 'Ioana', '321');

ALTER TABLE `users` ADD PRIMARY KEY (`id`);