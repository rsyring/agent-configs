# Ask Opus

If you are told to ask Opus about something, you can do that by running this command:

`mise run agent auggie -- --model opus4.7 --print --quiet "<YOUR_PROMPT>"`

You should generally fix anything Opus finds wrong and/or follow its advice. If you
strongly disagree, you may ignore Opus and document that you have done so.

## Guidance from Opus

When told to get guidance from Opus, assume the user isn't available, ask Opus for input
and/or post your questions to it instead.

## Opus Context / Repo Access

Opus is the Anthropic Opus model running through an Augment agent. It is sandboxed in a
docker container but does have read and write access to the repo, just like you do.

## Code Reviews from Opus

When told to get code reviews from Opus: whenever you think you are finished with your
work, before stopping for the user to review, ask Opus for a code review. Tell Opus to
"Make sure to follow your conditional instructions on code reviews."

Once you have made changes, repeat Opus code reviews until Opus is satisfied or you reach
an impasse.

## IMPORTANT: VS Code / Auggie Tooling

If you are an Auggie agent running in VS Code, do **not** rely on
`launch-process(..., wait=true)` or a Python subprocess wrapper to capture the review
text. In this environment those often return empty output because the command expects a
TTY.

Instead, do this:

1. launch the exact `mise run agent auggie -- ...` command with `wait=false`
2. poll with `read-process(..., wait=true, max_wait_seconds=15)`
3. if still running, repeat short polls until you get output or completion
4. exit if waiting more than 10 mins

Reason: Opus/API failures can occur early, but a long blocking wait can hide them for
minutes.
