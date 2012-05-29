
DELETE from  lime_settings_global where stg_name in ('email_account', 'email_password', 'siteadminbounce', 'sitename', 'siteadminemail', 'emailmethod', 'emailsmtphost', 'emailsmtpuser', 'emailsmtpssl', 'emailsmtppassword');
INSERT INTO `lime_settings_global` (`stg_name`,`stg_value`) VALUES("email_account", "$email_account");
INSERT INTO `lime_settings_global` (`stg_name`,`stg_value`) VALUES("email_password", "$email_password");
INSERT INTO `lime_settings_global` (`stg_name`,`stg_value`) VALUES("siteadminbounce", "$siteadminbounce");
INSERT INTO `lime_settings_global` (`stg_name`,`stg_value`) VALUES("sitename", "$sitename");
INSERT INTO `lime_settings_global` (`stg_name`,`stg_value`) VALUES("siteadminemail", "$siteadminemail");
INSERT INTO `lime_settings_global` (`stg_name`,`stg_value`) VALUES("emailmethod", "$emailmethod");
INSERT INTO `lime_settings_global` (`stg_name`,`stg_value`) VALUES("emailsmtphost", "$emailsmtphost");
INSERT INTO `lime_settings_global` (`stg_name`,`stg_value`) VALUES("emailsmtpuser", "$emailsmtpuser");
INSERT INTO `lime_settings_global` (`stg_name`,`stg_value`) VALUES("emailsmtpssl", "$emailsmtpssl");
INSERT INTO `lime_settings_global` (`stg_name`,`stg_value`) VALUES("emailsmtppassword", "$emailsmtppassword");


