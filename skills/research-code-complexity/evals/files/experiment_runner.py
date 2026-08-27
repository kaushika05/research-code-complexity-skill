"""Synthetic experiment runner fixture."""

def run(config, data, seed):
    if config["mode"] == "train":
        if config.get("normalize"):
            data = normalize(data)
        if config.get("augment"):
            data = augment(data, seed)
        if config.get("model") == "linear":
            result = fit_linear(data, seed)
        elif config.get("model") == "tree":
            result = fit_tree(data, seed)
        else:
            raise ValueError("unknown model")
    elif config["mode"] == "evaluate":
        if not config.get("checkpoint"):
            raise ValueError("checkpoint required")
        result = evaluate(data, config["checkpoint"])
    else:
        raise ValueError("unknown mode")
    if config.get("save"):
        save_result(result, config["output"])
    return result
