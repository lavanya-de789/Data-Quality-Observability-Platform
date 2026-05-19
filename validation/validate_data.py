import pandas as pd
import great_expectations as gx

df=pd.read_csv(
'data/raw/customers.csv'
)

gx_df=gx.from_pandas(df)

gx_df.expect_column_values_to_not_be_null(
'customer_id'
)

gx_df.expect_column_values_to_not_be_null(
'name'
)

gx_df.expect_column_values_to_not_be_null(
'city'
)

gx_df.expect_column_values_to_be_between(
'spend',
min_value=0
)

results=gx_df.validate()

print(results)

if results["success"]:

    df.to_parquet(
    'data/validated/customers.parquet',
    index=False
    )

    print(
    'validation passed'
    )

else:

    print(
    'validation failed'
    )
