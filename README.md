<img align="right" width="120" alt="rmotr.com" src="https://user-images.githubusercontent.com/7065401/45454218-80bee800-b6b9-11e8-97bb-bb5e7675f440.png">

# Coinmarketcap Advanced Features

In our [previous class](https://github.com/rmotr-curriculum/wdc-class-3-coinmarketcap-django-forms) we've added some features to the [https://coinmarketcap.com/](https://coinmarketcap.com/) clone that we've been implementing. Today we will keep augmenting it with some more Django functionalities. 🙌

The goal of this practice is to learn how use Django built-in features in order to have Authentication, Permissions, Sessions and Custom commands.

Those are very common useful tools that will help you while implementing any kind of application. The main idea is to make usage of the code provided by Django instead of implementing our own solution to those problems.

## 1) Authentication

For this first part, we'll make usage of the Authentication package provided by Django.

Just adding a new template under `templates/registration/login.html` and proper `accounts` URLs inside `coinmarketcap/urls.py`, we'll have our Authentication feature up and running

We'll also add a Log in button to our navbar. Everything should look like this:

<img width="775" alt="screen shot 2019-01-07 at 11 09 40" src="https://user-images.githubusercontent.com/2788551/50772576-0a984f80-126d-11e9-96ad-80ada8114fb1.png">

<img width="775" alt="screen shot 2019-01-07 at 11 10 48" src="https://user-images.githubusercontent.com/2788551/50772602-1be15c00-126d-11e9-8ae0-d33dcbf85e82.png">

In case we want to make a view only available for logged in users, we can use the `login_required` decorator provided by Django, as well as showing/hiding some components in the template based on `request.user.is_authenticated` attribute.

## 2) Permissions

Sometimes we want to grant access to some functionalities for certain group of users, and avoid them to other group. For example, in this case we want to allow creating a new Cryptocurrency only to `staff` users.

In order to restrict the access to certain view, we'll make usage of the `user_passes_test` decorator. This will receive a function (implemented by us) which should return a boolean value based on whatever logic we want. In this case we're just checking if the user is staff.

In a similar way that we did before, we can add some statements in the template to show/hide certain components. In this case it can be `request.user.is_staff`.

## 3) Sessions

For this part we'll implement a new feature that will allow ANY kind of user to add Cryptocurrencies to a `Favorites` list.

Cryptocurrencies marked as favorites will remain in the user's `Session` as long as it's logged in. Whenever the user logs out, the session will clear everything it has.

Final state of this part should look like this:

<img width="956" alt="screen shot 2019-01-07 at 11 28 36" src="https://user-images.githubusercontent.com/2788551/50773450-a1fea200-126f-11e9-9696-936857c66ff1.png">

<img width="791" alt="screen shot 2019-01-07 at 11 31 49" src="https://user-images.githubusercontent.com/2788551/50773539-deca9900-126f-11e9-84b1-f873dff84329.png">

## 4) Sign up

Even though Django `DOES NOT` provide built in functionalities regarding sign up forms for creating new users, we'll create our own one in just a few simple steps.

We'll need to implement a `SignUpForm` inside `cryptocoins/forms.py`, which will be rendered in a template under `templates/signup.html`.

In a `signup` view inside `cryptocoins/views.py` we'll handle the logic that is in charged of creating the user if the provided data is valid, and if so, it'll log the user in and redirect him to the index page.

<img width="616" alt="screen shot 2019-01-07 at 11 38 54" src="https://user-images.githubusercontent.com/2788551/50773892-dc1c7380-1270-11e9-9b49-5847829b3236.png">

## 5) Custom commands

In the same way we execute commands like `runserver`, `makemigrations`, etc, we can implement our own commands that can do whatever task we need.

For this part we'll implement a new custom command under `cryptocoins/management/commands/export_currencies_to_csv.py` that should be in charged of getting all the Cryptocurrencies stored in the database and export their data to a CSV formated file.

That's all! 🎉 We just did a fourth iteration to the Coinmarketcap clone, adding some more advanced functionalities of the Django framework.
