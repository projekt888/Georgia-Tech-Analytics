Attribute VB_Name = "Module1"
'Eric Roberts 2019

Sub run_calc()
    'load an array of worksheets
    Dim sheetz
    sheetz = Array("2016", "2015", "2014")
    
    'the "Challenge"
    For Each Sheet In sheetz
        'turn it on
        Worksheets(Sheet).Activate
        'run the program
        main_calc
    Next Sheet

End Sub

Function main_calc()

    'all the calculations are done here in this function
    
    Dim find_length As Double
    find_length = Find_Range()
    Dim summary_idx As Integer
    summary_idx = 2
    
    
    
    Dim ticker As String
    Dim yearly_volume As Double
    Dim first_price As Double
    Dim last_price As Double
    Dim price_change As Double

    'initial conditions
    yearly_volume = 0
    ticker = Cells(2, 1).Value
    first_price = Cells(2, 3).Value
     
    Cells(summary_idx, 9).Value = ticker
    write_summary_titles
    
    'go through list from 2 to find_length
    For i = 2 To find_length
        'calculate running metrics
        yearly_volume = yearly_volume + Cells(i, 7)
    
        If Cells(i + 1, 1).Value <> Cells(i, 1).Value Then
            'new ticker at i+1, we're done!
            'calculate end metrics
            last_price = Cells(i, 6).Value
            
            'print metrics for ticker
            'yearly volume
            Cells(summary_idx, 12).Value = yearly_volume
            Cells(summary_idx, 10).Value = last_price - first_price
            
            If first_price > 0 Then
                Cells(summary_idx, 11).Value = (last_price - first_price) / first_price
            Else
                Cells(summary_idx, 11).Value = 0 'or na or something.
            End If
              
            'now make new row
            summary_idx = summary_idx + 1
            
            ticker = Cells(i + 1, 1).Value
            Cells(summary_idx, 9).Value = ticker
            'reset all counters
            yearly_volume = 0
            first_price = Cells(i + 1, 3).Value
            
            
            
            
            
        Else
            'normal case
            'nothing
        End If
    Next i
    
    'the "hard" stuff
    write_summary_summary_titles
    summary (summary_idx)
    
    
    
    
End Function

Public Function Find_Range() As Double
    
    Dim count_rows As Double
    
    count_rows = 1
   
    While IsEmpty(Cells(count_rows, 1).Value) = False
       count_rows = count_rows + 1
    Wend
    
    Find_Range = count_rows - 1

End Function
Public Function write_summary_titles()
'Ticker  Yearly Change   Percent Change  Total Volume

    Cells(1, 9).Value = "Ticker"
    Cells(1, 10).Value = "Yearly Change"
    Cells(1, 11).Value = "Percent Change"
    Cells(1, 12).Value = "Total Volume"
End Function

Public Function write_summary_summary_titles()
'

    Cells(2, 14).Value = "Greatest % Increase"
    Cells(3, 14).Value = "Greatest % Decrease"
    Cells(4, 14).Value = "Greatest Total Volume"


    Cells(1, 15).Value = "Ticker"
    Cells(1, 16).Value = "Value"

    
End Function

Public Function summary(number_in_table As Integer)
    
    Dim greatest_inc As Double
    Dim greatest_dec As Double
    Dim greatest_vol As Double
    
    Dim greatest_inc_tick As String
    Dim greatest_dec_tick As String
    Dim greatest_vol_tick As String
    
    greatest_inc = 0
    greatest_dec = 0
    greatest_vol = 0
    
    For i = 2 To (number_in_table - 1)
    
        If (Cells(i, 11).Value) > greatest_inc Then
            'there's a new greatest inc
            greatest_inc = Cells(i, 11).Value
            greatest_inc_tick = Cells(i, 9).Value
        End If
        
        If (Cells(i, 11).Value) < greatest_dec Then
            'there's a new greatest dec
            greatest_dec = Cells(i, 11).Value
            greatest_dec_tick = Cells(i, 9).Value
        End If
        
        If (Cells(i, 12).Value) > greatest_vol Then
            'there's a new greatest vol
            greatest_vol = Cells(i, 12).Value
            greatest_vol_tick = Cells(i, 9).Value
        End If
    
    Next i
    
    'format the nice table
    Cells(2, 15).Value = greatest_inc_tick
    Cells(2, 16).Value = greatest_inc
    
    Cells(3, 15).Value = greatest_dec_tick
    Cells(3, 16).Value = greatest_dec
    
    Cells(4, 15).Value = greatest_vol_tick
    Cells(4, 16).Value = greatest_vol
    
End Function



