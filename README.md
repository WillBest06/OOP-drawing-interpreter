# OOP-drawing-interpreter
This project takes a text file as an input and interprets the contents to draw different shapes using the python turtle graphics library. 

Below are instructions for how to use the program correctly.

Software Requirements
---------------------

-   **Python 3.x**
  
-   Interpreter set to **3.14.0**

-   **Tkinter** must be installed.

File Requirements
-----------------

-   Files must be in **`.txt`** format.

-   File paths must be **relative** to the source code.

1\. Simple Parser
-----------------

This mode is for **Black & White** shapes with **Solid Borders**.

### Syntax

-   **Lowercase letters:** Represent *Unfilled* shapes.

-   **Uppercase letters:** Represent *Filled* Black shapes.

-   **Space:** Leaves the cell blank.

-   **New Line:** Starts a new row of shapes.

### Key

| **Character** | **Shape** | **Fill Status** |
| ------------- | --------- | ----------------|
|`s`|Square|Unfilled|
|`S`|Square|Filled|
|`t`|Triangle|Unfilled|
|`T`|Triangle|Filled|
|`c`|Circle|Unfilled|
|`C`|Circle|Filled|

### Example `.txt` content

```
stc
ST C
s c
```

2\. Complex Parser
------------------

This mode is for **RGB** shapes with **Dashed** or **Solid** borders.

### Syntax

The file must be formatted using a custom Comma Separated Values (CSV) format.

Each shape is defined using a 4 character code: [Shape][Border Type][Border Colour][Fill Colour]

1.  **First Character (Shape):**

    -   `s` = Square

    -   `t` = Triangle

    -   `c` = Circle

2.  **Second Character (Border Type):**

    -   `-` = Dashed

    -   `|` = Solid

3.  **Third Character (Border Colour):** Number from 0 to 9 representing a colour as shown in the colour table below).

4.  **Fourth Character (Fill Colour):** 0-9 Number from 0 to 9 representing a colour as shown in the colour table below).

**Blank Spaces:** To leave a cell blank put a single space between the commas.

**New lines** in the text file create a new row

### Colour Table (0-9)

| **Number** | **Colour** |
|------------|-----------|
|**0**|Black|
|**1**|Red|
|**2**|Blue|
|**3**|Green|
|**4**|Yellow|
|**5**|Purple|
|**6**|Orange|
|**7**|Pink|
|**8**|Brown|
|**9**|White|

### Example `.txt` content

```
s|01,t-23,c|90
t|45, ,s-87

```

-   `s|01`: Square with a Solid Black border and a Red fill.
-   `t-23`: Triangle with a Dashed Blue border and a Green fill.
-   ` `: Empty space.
