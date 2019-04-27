-- drop table lists
-- drop table users


CREATE TABLE Users (
    UserIDKey INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    UserID VARCHAR(100) UNIQUE,
    SessionCount SMALLINT
);
show engine innodb status;
CREATE TABLE Lists (
    ListWordID INT NOT NULL AUTO_INCREMENT,
    UserIDKey INT NOT NULL,
    `List` SMALLINT NOT NULL,
    Word NVARCHAR(100),
    `Order` SMALLINT,
    PRIMARY KEY (ListWordID , `List` , `Order`),
    FOREIGN KEY (UserIDKey)
        REFERENCES spelling.Users (UserListsUsersIDKey)
);


CREATE TABLE `Lists` (
  `ListWordID` int(11) NOT NULL AUTO_INCREMENT,
  `UserIDKey` int(11) NOT NULL,
  `List` smallint(6) NOT NULL,
  `Word` varchar(100) CHARACTER SET utf8 DEFAULT NULL,
  `Order` smallint(6) NOT NULL DEFAULT '0',
  PRIMARY KEY (`ListWordID`,`List`,`Order`),
  KEY `UserIDKey` (`UserIDKey`),
  CONSTRAINT `Lists_ibfk_1` FOREIGN KEY (`UserIDKey`) REFERENCES `Users` (`UserIDKey`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;
#insert into dbo.users (UserID, SessionCount) values ('testuser123',2)