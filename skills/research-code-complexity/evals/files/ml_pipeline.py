def prepare_and_fit(records, split_ids, scaler, model):
    train = [row for row in records if row["id"] in split_ids["train"]]
    test = [row for row in records if row["id"] in split_ids["test"]]
    if train:
        train_x = scaler.fit_transform([row["features"] for row in train])
    else:
        train_x = []
    if test:
        test_x = scaler.transform([row["features"] for row in test])
    else:
        test_x = []
    fitted = model.fit(train_x, [row["label"] for row in train])
    return fitted, fitted.predict(test_x)
