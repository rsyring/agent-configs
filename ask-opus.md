# Ask Opus

If you are told to ask Opus about something, you can do that by running this command:

`mise run agent auggie -- --model opus4.7 --print --quiet "<YOUR_PROMPT>"`

You should generally fix anything Opus finds wrong and/or follow it's advice. If you
strongly disagree, you may ignore Opus and document you have done so.

## Guidance from Opus

When told to get guidance from Opus, assume the user isn't available, ask Opus for input
and/or post your questions to it instead.

## Opus Context / Repo Access

Opus is the Antropic Opus model running through an Agument agent. It is sandboxed in a
docker container but does have read and write access to the repo, just like you do.

## Code Reviews from Opus

When told to get code reviews from Opus: whenever you think you are finished with your
work, before stopping for the user to review, ask Opus for a code review. Tell Opus to
"Make sure to follow your conditional instructions on code reviews."

Once you have made changes, repeate Opus code reviews until Opus is satisfied or you reach
an impasse.

## Opus guideance / reviews saved to files

Save any guidance or code reviews from Opus to a new file in `./tmp` named after the work
or spec you are doing and with numbers to indicate sequence.
