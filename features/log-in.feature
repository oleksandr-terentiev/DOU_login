Feature: Log-in on DOU.UA
    On the www.dou.ua
    User should be logged-in with right data
    User should not be logged-in with wrong data

    Scenario Outline: Positive log-in outline scenarios
        Given Particular browser <browser>
        When I input my login <login> and password <password> into the input fields
        Then I see my user icon in top right corner
        And After test browser must be closed

      Examples:
        | login	                    	| password  	| browser	|
        | 'alex.qa.engineer@gmail.com'	| '123456789d'	| CHROME   	|
        | 'alex.qa.engineer@gmail.com'	| '123456789d'	| OPERA   	|
        | 'alex.qa.engineer@gmail.com' 	| '123456789d'	| FIREFOX	|
        | 'alex.qa.engineer@gmail.com' 	| '123456789d'	| ANDROID	|

    Scenario Outline: Negative log-in scenarios with tables
        Given Particular browser <neg_browser>
        When I input wrong data, I'm not logged in:
          | login                        	| password      |
          | 'alex.qa.engineer@gmail.com' 	| '123456789d '	|
          | 'alex.qa.engineer.gmail.com' 	| ' 123456789d'	|
          | '<alex.qa.engineer@gmail.com>' 	| '123456789d'	|

      Examples:
        | neg_browser	|
        | CHROME	|
        | FIREFOX	|
        | OPERA 	|
        | ANDROID	|
