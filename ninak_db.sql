CREATE DATABASE 'ninak';

DROP TABLE IF EXISTS `account`;

CREATE TABLE `account` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(255) DEFAULT NULL,
  `password` varchar(255) DEFAULT NULL,
  `old_password` varchar(255) DEFAULT NULL,
  `wrong_login_attempt` int(11) DEFAULT NULL,
  `today_login_attempt` int(11) DEFAULT NULL,
  `is_now_login` int(1) DEFAULT NULL,
  `date` varchar(20) DEFAULT NULL,
  `time` time DEFAULT NULL,
  `timestamp` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=600855 DEFAULT CHARSET=utf8;


INSERT INTO account(username,password) values('rjzevallos.salazar@gmail.com','123456');
