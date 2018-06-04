### AWORK a CLI client for AWX

Awork is mainly a simplified demonstration of the core functionality of
tower-cli through the click library.

Awork stands for "Awork is not tower-cli". Don't ask me how that works.

```
awork foo bar 34 -b foobar
 root command:           awork (of course)
 resource category name: foo
 action name:            bar

 call args: ()
 call kwargs: {'pk': 34, 'baz': u'foobar'}
```

This is a basic example to show the command resolution of awork, and
also of tower-cli.

 - `foo` is a subcommand of the main entry point
 - `bar` is a subcommand of `foo`, which is the "action" part of the command
 - `-b` is an option
 - `pk` is an argument

#### Prohibited items

These things will not be used here:

 - decorators
 - metaclasses
 - in-line imports

#### Legal

This is not sponsored by any company or anything like that.

I just made the repository on my own, it is not in intended for _use_
at all.
