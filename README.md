ZADANIE 2: selektory

1.Scouts Panel

/html/body/div/form/div/div[1]/h5 \
h5.MuiTypography-root\
//*[text()="Scouts Panel"]

2.Login

//label[@id="password-label"] \
//label[@for="login"]\
#login-label 

3.Miejsce do wpisania loginu

//input[@id="login"] \
//input[@type="text"] \
/input[@name="login"] 

4.Password

//label[@id="password-label"]\
//label[@for="password"]\
#password-label


5.Miejsce do wpisania hasła

//input[@id="password"] \
//input[@type="password"] \
//input[@name="password"] 


6.English

//div[@role="button"]\
//div[@aria-haspopup="listbox"]\
//div[@tabindex="0"]

7.Sign in

//span[@class="MuiButton-label"]\
//span[@class="MuiTouchRipple-root"]\
[class="MuiButton-label"]