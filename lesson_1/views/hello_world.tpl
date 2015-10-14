<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"
        "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
    <title>Bottle example</title>
</head>
<body>
<p> Hello {{username}}! </p>

Your things are:
<ul>
    %for thing in things:
    <li>{{thing}}</li>
    %end
</ul>
<form action="/favourite_thing" method="POST">
      Whats your favourite thing?
    <input type="text" name="thing" value=""><br>
    <input type="submit" value="Submit">
</form>


</body>
</html>