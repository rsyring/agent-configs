# Python CLI Instructions - General

- Prefer Click for CLIs
- Prefer rich (the library) for tabular or other complex output

## Typed Click context objects

If commands need a config or similar global object, set that up with `click.make_pass_decorator`. We
prefer passing in a typed object to the command function.

```python

@dataclass
class Config:
    ssh_user: str
    ssh_root: str = ''

pass_config = click.make_pass_decorator(Config)

@click.group()
@click.option('--ssh-dest', type=str, default=environ.get('ZOR_SSH_DEST', ''))
@click.pass_context
def cli(ctx: click.Context, ssh_dest: str):
    if not ssh_dest:
        raise click.ClickException('Set ZOR_SSH_DEST or use --ssh-dest')

    ctx.obj = Config(ssh_dest)

@cli.command()
@pass_config
def ssh_copy_id(conf: Config):
    """Run 1st"""
    assert conf
```
