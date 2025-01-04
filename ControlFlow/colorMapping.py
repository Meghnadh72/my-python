colors = ['b', 'br', 'y', 'r', 'bl', 'w', 'pu']
color_input = input('Enter Color code')
match color_input:
    case 'b':
        output_color = 'blue'
    case 'br':
        output_color = 'brown'
    case default:
        output_color = "No matching Color"
print(output_color)