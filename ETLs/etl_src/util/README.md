## schema_inferences class

Seeing as there are around 400 input columns I wrote this class as a quick way of getting the schemas and creating the tables.  
Since this is just a pretend exercise I'm letting Pandas do the work for me here.

If this was a real ETL schema state could be maintained and enforced by either:

1) tracking internally to the ETL application, which is what I implemented in the schemas folder.  Ex:
``` python
{table_1: {col_1: str,
          col_2: Decimal,
          col_3, Int,
          etc...
          }
}
code would look something like:

for col, value in input_data_row.items():
    converted_value = state_table[col](value)
 
or
``` 
2) Build or use an external schema tracking tool like Confluent Schema Registry

