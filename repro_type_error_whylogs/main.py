from whylogs.core import DatasetProfile

profile = DatasetProfile()
profile.track({'a': 2})
print(profile.view().to_pandas())

