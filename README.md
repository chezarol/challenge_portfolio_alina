<h1 align="center">Task 1: Software configuration</h1>
<h2 align="center">Subtask 1: "Why did I choose to participate in the challenge portfolio?"</h2>

*Hi, my name's Alina. I've made up my mind to take part in the challenge because I'm professionally burnt out. Quite frankly, I've never liked my job. It may sound stupid, but it's been a dream since my childhood to work in IT. And now I'm happy to have an opportunity to make my dream come true.*
 
*I expect to get new knowledge, experience, friends and job. They are precious for me.*
 
*ALINA*


<h1 align>Task 2: "Selectors"</h1>

**//*[@id="__next"]/form/div/div[1]/h5**
<ol>
<li>//*[text()="Scouts Panel"]</li>
<li>//h5</li>
<li>//*[@id="__next"]/form/div/div[1]/descendant::h5</li>
</ol>


**//*[@id="__next"]/form/div/div[1]/div[1]**
<ol>
<li>//*[@id="login"]</li>
<li>//*[@name="login"]</li>
<li>//input [@id="login"] </li>
</ol>


**//*[@id="password"]**
<ol>
<li>//*[@name="password"]</li>
<li>//input[@id="password"]</li>
<li>//*[@id="__next"]/form/div/div[1]/div[2]/div/descendant::input</li>
</ol>


**//*[@id="__next"]/form/div/div[1]/a**
<ol> 
<li>//*[text()="Remind password"]</li>
<li>//*[contains(@class, "MuiTypography-root MuiLink")]</li>
<li>//child::div/a</li>
</ol>


**//*[@id="__next"]/form/div/div[2]/div/div**
<ol> 
<li>//*[text()="English"]</li>
<li>//*[@id="__next"]/form/div/div[2]/div/input/preceding-sibling::*</li>
</ol>



**//*[@id="__next"]/form/div/div[2]/div/div**
<ol> 
<li>//*[text()="Polski"]</li>
<li>//*[@id="__next"]/form/div/div[2]/div/input/preceding-sibling::*</li>
</ol>



**//*[@id="__next"]/form/div/div[2]/button/span[1]**
<ol> 
<li>//*[@class="MuiButton-label"]</li>
<li>//*[text()="Sign in"]</li>
<li>//span[@class="MuiButton-label"]</li>
</ol>