"""
Custom Pygments style for electronics/engineering code
Based on the default style but with custom colors for technical content
"""

from pygments.style import Style
from pygments.token import (
    Token, Comment, Keyword, Name, String, Number, Operator,
    Punctuation, Generic, Whitespace, Error
)

class ElectronicsStyle(Style):
    """
    Custom style for electronics and engineering code
    """
    
    name = 'electronics'
    
    styles = {
        Token:                '#2E8B57',  # Dark sea green - main text
        Whitespace:           '#bbbbbb',
        
        Comment:              'italic #008000',     # Green comments
        Comment.Preproc:      '#008080',           # Teal preprocessor
        Comment.Special:      'bold #008000',      # Bold green for special comments
        
        Keyword:              'bold #1f77b4',      # Blue keywords
        Keyword.Pseudo:       '#1f77b4',
        Keyword.Type:         '#d62728',           # Red for types
        
        Operator:             '#d62728',           # Red operators
        Operator.Word:        'bold #d62728',
        
        Punctuation:          '#2E8B57',
        
        Name:                 '#2E8B57',
        Name.Attribute:       '#ff7f0e',           # Orange attributes
        Name.Builtin:         '#1f77b4',           # Blue builtins
        Name.Builtin.Pseudo:  '#1f77b4',
        Name.Class:           'bold #9467bd',      # Purple classes
        Name.Constant:        '#d62728',           # Red constants
        Name.Decorator:       '#ff7f0e',           # Orange decorators
        Name.Entity:          '#ff7f0e',
        Name.Exception:       'bold #d62728',      # Bold red exceptions
        Name.Function:        '#9467bd',           # Purple functions
        Name.Property:        '#ff7f0e',
        Name.Label:           '#2E8B57',
        Name.Namespace:       '#9467bd',
        Name.Other:           '#2E8B57',
        Name.Tag:             'bold #1f77b4',      # Bold blue tags
        Name.Variable:        '#2E8B57',
        Name.Variable.Class:  '#2E8B57',
        Name.Variable.Global: '#2E8B57',
        Name.Variable.Instance: '#2E8B57',
        
        Number:               '#8c564b',           # Brown numbers
        Number.Float:         '#8c564b',
        Number.Hex:           '#8c564b',
        Number.Integer:       '#8c564b',
        Number.Integer.Long:  '#8c564b',
        Number.Oct:           '#8c564b',
        
        String:               '#2ca02c',           # Green strings
        String.Backtick:      '#2ca02c',
        String.Char:          '#2ca02c',
        String.Doc:           'italic #2ca02c',    # Italic green docstrings
        String.Double:        '#2ca02c',
        String.Escape:        'bold #8c564b',      # Bold brown escapes
        String.Heredoc:       '#2ca02c',
        String.Interpol:      'bold #2ca02c',
        String.Other:         '#2ca02c',
        String.Regex:         '#2ca02c',
        String.Single:        '#2ca02c',
        String.Symbol:        '#2ca02c',
        
        Generic:              '#2E8B57',
        Generic.Deleted:      '#d62728',           # Red for deleted
        Generic.Emph:         'italic',
        Generic.Error:        '#d62728',           # Red errors
        Generic.Heading:      'bold #1f77b4',      # Bold blue headings
        Generic.Inserted:     '#2ca02c',           # Green for inserted
        Generic.Output:       '#2E8B57',
        Generic.Prompt:       'bold #9467bd',      # Bold purple prompts
        Generic.Strong:       'bold',
        Generic.Subheading:   'bold #9467bd',
        Generic.Traceback:    '#d62728',           # Red tracebacks
        
        Error:                'border:#d62728'     # Red border for errors
    }


class SPICEStyle(Style):
    """
    Custom style specifically for SPICE code
    """
    
    name = 'spice'
    
    styles = {
        Token:                '#2E3440',  # Dark blue-gray
        Whitespace:           '#D8DEE9',
        
        Comment:              'italic #616E88',    # Muted blue comments
        Comment.Preproc:      '#5E81AC',           # Blue preprocessor
        
        Keyword:              'bold #81A1C1',      # Light blue keywords
        Keyword.Type:         '#BF616A',           # Red types
        
        Operator:             '#EBCB8B',           # Yellow operators
        Punctuation:          '#ECEFF4',
        
        Name:                 '#D8DEE9',           # Light gray names
        Name.Builtin:         '#88C0D0',           # Cyan builtins
        Name.Function:        '#8FBCBB',           # Teal functions
        Name.Variable:        '#D8DEE9',
        
        Number:               '#B48EAD',           # Purple numbers
        String:               '#A3BE8C',           # Green strings
        
        Generic.Output:       '#D8DEE9',
        Generic.Prompt:       'bold #5E81AC',      # Bold blue prompts
        
        Error:                'border:#BF616A'     # Red border
    }