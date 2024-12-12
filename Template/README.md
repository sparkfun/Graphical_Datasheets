### Creating a New Graphical Datasheet using the Template

The template was created for those that are not using Python to generate the cells on a Graphical Datasheet. The template is also formatted and includes logos, legend, lines, and text for the product title, SKU and features. 

1. In the **Template** folder, open the **2-SparkFun_Graphical_Datasheet-Template.svg**.
2. Save as a new file based on the development board. You may need to place the file in a new folder.
3. Replace the AzureWave Thing Plus AW-CU488 Development Board. If necessary, create a rectangle object over the board. Under **Object** > **Objects...** Then highlight the rectangle and product photo. Right click on the layers and select **Set Clip**.. This will "crop" the image without deleting any of the original image.
4. Fill in the pin labels with the microcontroller's pin function. If possible, try to group the pins in the same column.
5. Adjust the cell color based on the pin function. Select the cell(s) and change the Fill & Stroke's RGBA under **Object** > **Fill and Stroke...**
    * Note: Check out the Color Table below!
6. In the objects, hide any unused text and cells.
    * Note: While you can delete each unused text and cell, you will need to duplicate the objects and re-align it with the rest of the pins if a pin functionality was missing.
7. Update the legend.
8. Select the group of cells and lines and align them with the development board pinout.
    * Note: Careful when resizing and adjust the font. The text can be hard to read if it is too small.
9. Adjust the product name, SKU, and features.
10. If necessary, draw additional lines and label any parts of the board that you would like to highlight (i.e. buttons, connectors, ICs).
11. Add any additional images of the board (i.e. jumpers, ICSP, SWD pins) that you would like to highlight.
12. Move any objects (i.e. logos, features, legend) around so that the layers are not overlapping over each other.
    * Note: If necessary, add a second page if there is not enough room on the page! Type in a corner the page number (i.e. 1/2 or 2/2).



### Color Table

<!-- Fritzing Graphic Standards => https://fritzing.org/fritzings-graphic-standards -->

<div style="text-align: center;">
    <table>
        <tr>
            <th style="text-align: center; border: solid 1px #cccccc;">Pin
            </th>
            <th style="text-align: center; border: solid 1px #cccccc;">Text Font Color
            </th>
            <th style="text-align: center; border: solid 1px #cccccc;">Hex and Alpha Values
            </th>
            <th style="text-align: center; border: solid 1px #cccccc;"Color>Cell Color</th>
            <th style="text-align: center; border: solid 1px #cccccc;">Hex and Alpha Values
            </th>
        </tr>
        <tr>
            <td style="text-align: center; border: solid 1px #cccccc;" bgcolor="#ffffff">Name
            </td>
            <td style="text-align: center; border: solid 1px #cccccc;">Black
            </td>
            <td style="text-align: center; border: solid 1px #cccccc;" bgcolor="#ffffff">000000ff
            </td>
            <td style="text-align: center; border: solid 1px #cccccc;">White (with Gray Outline)
            </td>
            <td style="text-align: center; border: solid 1px #cccccc;" bgcolor="#ffffff">ffffffff
            </td>
        </tr>
        <tr>
            <td style="text-align: center; border: solid 1px #cccccc;" bgcolor="#ff4949">Power
            </td>
            <td style="text-align: center; border: solid 1px #cccccc;">Black
            </td>
            <td style="text-align: center; border: solid 1px #cccccc;" bgcolor="#ffffff">000000ff
            </td>
            <td style="text-align: center; border: solid 1px #cccccc;" bgcolor="#ff4949">Red
            </td>
            <td style="text-align: center; border: solid 1px #cccccc;" bgcolor="#ff4949">ff4949ff
            </td>
        </tr>
        <tr>
            <td style="text-align: center; border: solid 1px #cccccc;" bgcolor="#000000"><font color="#ffffff">Ground</font>
            </td>
            <td style="text-align: center; border: solid 1px #cccccc;">White
            </td>
            <td style="text-align: center; border: solid 1px #cccccc;" bgcolor="#ffffff">ffffffff
            </td>
            <td style="text-align: center; border: solid 1px #cccccc;" bgcolor="#000000"><font color="#ffffff">Black</font>
            </td>
            <td style="text-align: center; border: solid 1px #cccccc;" bgcolor="#000000"><font color="#ffffff">000000ff</font>
            </td>
        </tr>
        <tr>
            <td style="text-align: center; border: solid 1px #cccccc;" bgcolor="#ffff4d">Control
            </td>
            <td style="text-align: center; border: solid 1px #cccccc;">Black
            </td>
            <td style="text-align: center; border: solid 1px #cccccc;" bgcolor="#ffffff">000000ff
            </td>
            <td style="text-align: center; border: solid 1px #cccccc;" bgcolor="#ffff4d">Yellow
            </td>
            <td style="text-align: center; border: solid 1px #cccccc;" bgcolor="#ffff4d">ffff4dff
            </td>
        </tr>
        <tr>
            <td style="text-align: center; border: solid 1px #cccccc;" bgcolor="#b3b3b3">Port
            </td>
            <td style="text-align: center; border: solid 1px #cccccc;">Black
            </td>
            <td style="text-align: center; border: solid 1px #cccccc;" bgcolor="#ffffff">000000ff
            </td>
            <td style="text-align: center; border: solid 1px #cccccc;" bgcolor="#b3b3b3">Grey
            </td>
            <td style="text-align: center; border: solid 1px #cccccc;" bgcolor="#b3b3b3">b3b3b3ff
            </td>
        </tr>
        <tr>
            <td style="text-align: center; border: solid 1px #cccccc;" bgcolor="#b3d9b2">Arduino Pin Reference
            </td>
            <td style="text-align: center; border: solid 1px #cccccc;">Black
            </td>
            <td style="text-align: center; border: solid 1px #cccccc;" bgcolor="#ffffff">000000ff
            </td>
            <td style="text-align: center; border: solid 1px #cccccc;" bgcolor="#b3d9b2">Light Green
            </td>
            <td style="text-align: center; border: solid 1px #cccccc;" bgcolor="#b3d9b2">b3d9b2ff
            </td>
        </tr>
        <tr>
            <td style="text-align: center; border: solid 1px #cccccc;" bgcolor="#cb99cc">ADC
            </td>
            <td style="text-align: center; border: solid 1px #cccccc;">Black
            </td>
            <td style="text-align: center; border: solid 1px #cccccc;" bgcolor="#ffffff">000000ff
            </td>
            <td style="text-align: center; border: solid 1px #cccccc;" bgcolor="#cb99cc">Purple
            </td>
            <td style="text-align: center; border: solid 1px #cccccc;" bgcolor="#cb99cc">cb99ccff
            </td>
        </tr>
        <tr>
            <td style="text-align: center; border: solid 1px #cccccc;" bgcolor="#4286f5">UART
            </td>
            <td style="text-align: center; border: solid 1px #cccccc;">Black
            </td>
            <td style="text-align: center; border: solid 1px #cccccc;" bgcolor="#ffffff">000000ff
            </td>
            <td style="text-align: center; border: solid 1px #cccccc;" bgcolor="#4286f5">Blue
            </td>
            <td style="text-align: center; border: solid 1px #cccccc;" bgcolor="#4286f5">4286f5ff
            </td>
        </tr>        
        <tr>
            <td style="text-align: center; border: solid 1px #cccccc;" bgcolor="#ff7007">I2C
            </td>
            <td style="text-align: center; border: solid 1px #cccccc;">Black
            </td>
            <td style="text-align: center; border: solid 1px #cccccc;" bgcolor="#ffffff">000000ff
            </td>
            <td style="text-align: center; border: solid 1px #cccccc;" bgcolor="#ff7007">Dark Orange
            </td>
            <td style="text-align: center; border: solid 1px #cccccc;" bgcolor="#ff7007">ff7007ff
            </td>
        </tr>    
        <tr>
            <td style="text-align: center; border: solid 1px #cccccc;" bgcolor="#fabd03">SPI
            </td>
            <td style="text-align: center; border: solid 1px #cccccc;">Black
            </td>
            <td style="text-align: center; border: solid 1px #cccccc;" bgcolor="#ffffff">000000ff
            </td>
            <td style="text-align: center; border: solid 1px #cccccc;" bgcolor="#fabd03">Light Orange
            </td>
            <td style="text-align: center; border: solid 1px #cccccc;" bgcolor="#fabd03">fabd03ff
            </td>
        </tr>    
        <tr>
            <td style="text-align: center; border: solid 1px #cccccc;" bgcolor="#fffeb1">Ext Int
            </td>
            <td style="text-align: center; border: solid 1px #cccccc;">Black
            </td>
            <td style="text-align: center; border: solid 1px #cccccc;" bgcolor="#ffffff">000000ff
            </td>
            <td style="text-align: center; border: solid 1px #cccccc;" bgcolor="#fffeb1">Light Yellow
            </td>
            <td style="text-align: center; border: solid 1px #cccccc;" bgcolor="#fffeb1">fffeb1ff
            </td>
        </tr>    
        <tr>
            <td style="text-align: center; border: solid 1px #cccccc;" bgcolor="#34a853"><font color="000000">PC Int</font>
            </td>
            <td style="text-align: center; border: solid 1px #cccccc;">White
            </td>
            <td style="text-align: center; border: solid 1px #cccccc;" bgcolor="#ffffff">ffffffff
            </td>
            <td style="text-align: center; border: solid 1px #cccccc;" bgcolor="#34a853"><font color="000000">Forest Green/Dark Green</font>
            </td>
            <td style="text-align: center; border: solid 1px #cccccc;" bgcolor="#34a853"><font color="000000">34a853ff</font>
            </td>
        </tr><tr>
            <td style="text-align: center; border: solid 1px #cccccc;" bgcolor="#005544">USB
            </td>
            <td style="text-align: center; border: solid 1px #cccccc;">White
            </td>
            <td style="text-align: center; border: solid 1px #cccccc;" bgcolor="#ffffff">ffffffff
            </td>
            <td style="text-align: center; border: solid 1px #cccccc;" bgcolor="#005544"><font color="ffffff">Hunter Green</font>
            </td>
            <td style="text-align: center; border: solid 1px #cccccc;" bgcolor="#005544"><font color="ffffff">005544ff</font>
            </td>
        </tr>
        <tr>
            <td style="text-align: center; border: solid 1px #cccccc;" bgcolor="#ffdfe5">CAN
            </td>
            <td style="text-align: center; border: solid 1px #cccccc;">Black
            </td>
            <td style="text-align: center; border: solid 1px #cccccc;" bgcolor="#ffffff">000000ff
            </td>
            <td style="text-align: center; border: solid 1px #cccccc;" bgcolor="#ffdfe5">Pink
            </td>
            <td style="text-align: center; border: solid 1px #cccccc;" bgcolor="#ffdfe5">ffdfe5ff
            </td>
        </tr>       
        <tr>
            <td style="text-align: center; border: solid 1px #cccccc;" bgcolor="#46bdc6">Audio
            </td>
            <td style="text-align: center; border: solid 1px #cccccc;">Black
            </td>
            <td style="text-align: center; border: solid 1px #cccccc;" bgcolor="#ffffff">000000ff
            </td>
            <td style="text-align: center; border: solid 1px #cccccc;" bgcolor="#46bdc6">Turquoise
            </td>
            <td style="text-align: center; border: solid 1px #cccccc;" bgcolor="#46bdc6">46bdc6ff
            </td>
        </tr>    
        <tr>
            <td style="text-align: center; border: solid 1px #cccccc;" bgcolor="#cdcefe">Misc
            </td>
            <td style="text-align: center; border: solid 1px #cccccc;">Black
            </td>
            <td style="text-align: center; border: solid 1px #cccccc;" bgcolor="#ffffff">000000ff
            </td>
            <td style="text-align: center; border: solid 1px #cccccc;" bgcolor="#cdcefe">Lavender/Light Purple
            </td>
            <td style="text-align: center; border: solid 1px #cccccc;" bgcolor="#cdcefe">cdcefeff
            </td>
        </tr>
    </table>
</div>
