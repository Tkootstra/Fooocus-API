from pathlib import Path


checkpoint_source = Path("/data/checkpoints")
lora_source = Path("/data/loras")

checkpoint_dest = Path("/app/repositories/Fooocus/models/checkpoints")
lora_dest = Path("/app/repositories/Fooocus/models/loras")


for root in [checkpoint_source, lora_source]:
    for pt in checkpoint_source.iterdir():
        if pt.is_file():
            name = pt.name
            dest = checkpoint_dest / name
            if not dest.exists():
                pt.symlink_to(target=dest)