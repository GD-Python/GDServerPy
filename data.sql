CREATE TABLE accounts (
  userName varchar(20) NOT NULL,
  password varchar(256) NOT NULL,
  email varchar(80) NOT NULL,
  accountID int(11) NOT NULL,
  isAdmin int(11) NOT NULL DEFAULT 0,
  mS int(11) NOT NULL DEFAULT 0,
  frS int(11) NOT NULL DEFAULT 0,
  cS int(11) NOT NULL DEFAULT 0,
  youtube varchar(255) NOT NULL DEFAULT '',
  twitter varchar(255) NOT NULL DEFAULT '',
  twitch varchar(255) NOT NULL DEFAULT '',
  salt varchar(255) NOT NULL DEFAULT '',
  registerDate int(11) NOT NULL DEFAULT 0,
  friendsCount int(11) NOT NULL DEFAULT 0,
  discordID bigint(20) NOT NULL DEFAULT 0,
  discordLinkReq bigint(20) NOT NULL DEFAULT 0,
  isActive tinyint(1) NOT NULL DEFAULT 0
)