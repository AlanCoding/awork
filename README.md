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

#### Headline features of rewrite

These are the user-facing more important features that this is trying to sell:

 - No manual maintaining of fields list
 - Tower version and API version switchable by server or user
 - Accurate handling of uniqueness rules, no duplicate specification

#### Code structure points

Prohibited items:

 - decorators
 - metaclasses
 - minimal in-line imports

You could say that part of this refactor had already begun with the
divorcing of the models/resources from the cli folder, where the command
classes became logically organized in terms of root command, resource
command, and then action command.

This rewrite is intended to destroy the `tower_cli/resources` folder
entirely, replacing it with `tower_cli/schema`.

For now, the schema is generated (`make schema`), but the idea is that
eventually, a more comprehensive schema could be officially published,
and that would be used instead.

Still to do goal: _Nothing_ in the cli folders are to do anything
programatically non-trivial that is unconnected to the CLI interface.
Instead, all _functional_ interactions with the server will go
in the `tower_cli/models`, so that CLI users are not privileged over
the python users.

#### Legal

This is not sponsored by any company or anything like that.

I just made the repository on my own, it is not in intended for _use_
at all.

### Timings

As of 2nd commit, with zip_safe off:

```
real	0m0.232s
user	0m0.142s
sys	0m0.062s
```

With zip_safe on:

```
real	0m0.187s
user	0m0.133s
sys	0m0.050s
```

