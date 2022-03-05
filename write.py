import aspose.words as aw

# Create a new Word document.
doc = aw.Document()

# Create document builder.
builder = aw.DocumentBuilder(doc)

# Start the table.
table = builder.start_table()

# Insert cell.
builder.insert_cell()

# Table wide formatting must be applied after at least one row is present in the table.
table.left_indent = 20.0

# Set height and define the height rule for the header row.
builder.row_format.height = 40.0
builder.row_format.height_rule = aw.HeightRule.AT_LEAST

# Set alignment and font settings.
builder.paragraph_format.alignment = aw.ParagraphAlignment.CENTER
builder.font.size = 16
builder.font.name = "Arial"
builder.font.bold = True

builder.cell_format.width = 100.0
builder.write("Header Row,\n Cell 1")

# We don't need to specify this cell's width because it's inherited from the previous cell.
builder.insert_cell()
builder.write("Header Row,\n Cell 2")

builder.insert_cell()
builder.cell_format.width = 200.0
builder.write("Header Row,\n Cell 3")
builder.end_row()

builder.cell_format.width = 100.0
builder.cell_format.vertical_alignment = aw.tables.CellVerticalAlignment.CENTER

# Reset height and define a different height rule for table body.
builder.row_format.height = 30.0
builder.row_format.height_rule = aw.HeightRule.AUTO
builder.insert_cell()

# Reset font formatting.
builder.font.size = 12
builder.font.bold = False

builder.write("Row 1, Cell 1 Content")
builder.insert_cell()
builder.write("Row 1, Cell 2 Content")

builder.insert_cell()
builder.cell_format.width = 200.0
builder.write("Row 1, Cell 3 Content")
builder.end_row()

builder.insert_cell()
builder.cell_format.width = 100.0
builder.write("Row 2, Cell 1 Content")

builder.insert_cell()
builder.write("Row 2, Cell 2 Content")

builder.insert_cell()
builder.cell_format.width = 200.0
builder.write("Row 2, Cell 3 Content.")
builder.end_row()

# End table.
builder.end_table()

# Save the document.
doc.save("table_formatted.docx")