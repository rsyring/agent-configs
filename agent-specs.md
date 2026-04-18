# Specs & Execution Plans

When instructions reference a "spec", that refers to a living document we will use to make progress
on a project.  You should keep it updated so it serves as a record of our findings, decisions, and
actions taken.

If given the command "read spec" or "process spec", you should read the file given, or it may already
be in your context.

Upon receipt of either command, you should:

- Read the spec file
- Respond to the user with "Spec file {name of spec file} found."
- Add any questions you have to the spec file.  Don't force questions; if there aren't any, skip
  this step.  If you've added questions, prompt the user to answer them.
- If there are no questions, or once the questions are answered, ask the user for permission to start
  working on the spec.
