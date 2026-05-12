# Enhanced Node Details with Error Warnings

## Overview

The web interface now displays **detailed error warnings** when you click on a node in the graph. Previously, it only showed basic node information. Now it provides comprehensive diagnostic information about any issues associated with that specific node.

---

## What Changed

### Files Modified:
- **`web/index.html`** - Enhanced node click handler and added warning display logic

### New Features:
1. ✅ **Line number display** - Shows the source line number for each node
2. ✅ **Error warnings section** - Displays all errors associated with the clicked node
3. ✅ **Visual indicators** - Color-coded warnings with icons for different error types
4. ✅ **Actionable advice** - Each warning includes specific recommendations for fixing the issue

---

## Warning Types

### 1. 🚫 Unreachable Node (Недостижимый узел)
**Icon**: 🚫  
**Color**: Gray (#8e8e93)

**When shown**: Node cannot be reached from the `start` label

**Example**:
```
⚠️ Предупреждения:

🚫 Недостижимый узел
Этот узел недостижим из начальной точки. Добавьте переход к нему 
или удалите, если он не нужен.
```

---

### 2. ❌ Missing Reference (Ошибка перехода)
**Icon**: ❌  
**Color**: Orange (#ff9500)

**When shown**: Node is referenced by a jump/call but doesn't exist in the script

**Example**:
```
⚠️ Предупреждения:

❌ Ошибка перехода
Ссылка на этот узел существует, но сам узел не найден в графе. 
Проверьте правильность jump/call.
```

---

### 3. 🔄 Infinite Loop (Бесконечный цикл)
**Icon**: 🔄  
**Color**: Yellow (#ffcc00)

**When shown**: Node is part of an infinite loop

**Example**:
```
⚠️ Предупреждения:

🔄 Бесконечный цикл
Этот узел участвует в бесконечном цикле. Добавьте условие выхода 
из цикла (например, проверку переменной или menu).
```

---

### 4. ⚠️ State Error (Ошибка состояния)
**Icon**: ⚠️  
**Color**: Purple (#af52de)

**When shown**: Node has an impossible condition (e.g., requires strength >= 50 but max is 18)

**Example**:
```
⚠️ Предупреждения:

⚠️ Ошибка состояния
Требуется strength ≥ 50, но максимум: 18.
Путь: start → home → training.
Решение: снизьте порог или добавьте больше выборов, дающих очки опыта.
```

---

## Before vs After Comparison

### **Before:**
```
Узел: secret_loop

Описание:
→ secret_loop

Код:
Jump(target='secret_loop', line=153, column=10)
```

### **After:**
```
Узел: secret_loop
Строка: 153

Описание:
→ secret_loop

Код:
Jump(target='secret_loop', line=153, column=10)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
⚠️ Предупреждения:

🔄 Бесконечный цикл
Этот узел участвует в бесконечном цикле. Добавьте условие выхода 
из цикла (например, проверку переменной или menu).
```

---

## Complex Example: Node with Multiple Errors

If a node has multiple issues, **all warnings are displayed**:

```
Узел: training
Строка: 93

Описание:
if strength >= 50
→ chapter2

Код:
Condition(var='strength', op='>=', value=50, ...)
Jump(target='chapter2', line=95, column=10)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
⚠️ Предупреждения:

⚠️ Ошибка состояния
Требуется strength ≥ 50, но максимум: 18.
Путь: start → home → training.
Решение: снизьте порог или добавьте больше выборов, дающих очки опыта.

🚫 Недостижимый узел
Этот узел недостижим из начальной точки. Добавьте переход к нему 
или удалите, если он не нужен.
```

---

## Implementation Details

### Key Functions Added:

#### `getNodeWarnings(nodeId, analysis)`
Analyzes all error types for a specific node and returns an array of warning objects.

**Parameters**:
- `nodeId`: The ID of the clicked node
- `analysis`: The analysis results from the API

**Returns**: Array of warning objects with structure:
```javascript
{
  icon: '🔄',           // Emoji icon
  title: 'Бесконечный цикл',  // Warning title
  details: '...',       // Detailed explanation with fix advice
  bgColor: 'rgba(...)', // Background color for the warning box
  borderColor: '#...'   // Border color matching error type
}
```

### Data Flow:

```
1. User clicks node in graph
   ↓
2. Click handler triggered
   ↓
3. getNodeWarnings() called with node ID and analysis data
   ↓
4. Checks all error types:
   - Unreachable nodes
   - Missing references
   - Infinite loops
   - State errors
   ↓
5. Builds HTML with warnings
   ↓
6. Displays in "Детали узла" panel
```

---

## Visual Design

### Warning Box Styling:
- **Background**: Semi-transparent color matching error type (10% opacity)
- **Border**: Left border with solid color (3px)
- **Icon**: Emoji for quick visual recognition
- **Title**: Bold text with error name
- **Details**: Smaller text with explanation and fix advice

### Color Scheme:
- 🚫 Unreachable: Gray `#8e8e93`
- ❌ Missing: Orange `#ff9500`
- 🔄 Infinite Loop: Yellow `#ffcc00`
- ⚠️ State Error: Purple `#af52de`

---

## User Experience Improvements

### **Before Enhancement:**
- ❌ No information about why a node is highlighted
- ❌ User had to cross-reference with the report panel
- ❌ No actionable guidance on how to fix issues
- ❌ Confusing for new users

### **After Enhancement:**
- ✅ Immediate feedback when clicking any node
- ✅ All errors for that node shown in one place
- ✅ Specific recommendations for fixing each issue
- ✅ Visual indicators make errors easy to understand
- ✅ Context-aware (only shows relevant warnings)

---

## Testing

### Test Cases:

1. **Click on normal node** → No warnings shown ✅
2. **Click on unreachable node** → Shows unreachable warning ✅
3. **Click on loop node** → Shows infinite loop warning ✅
4. **Click on state error node** → Shows state error with details ✅
5. **Click on node with multiple errors** → Shows all warnings ✅

### Example Test:

Load `huge_branching.rpy` and click on these nodes:

| Node | Expected Warnings |
|------|------------------|
| `secret_loop` | 🔄 Infinite loop |
| `training` | ⚠️ State error (strength >= 50) |
| `reading` | ⚠️ State error (intelligence >= 50) |
| `forest_fight` | ⚠️ State error (strength >= 20) |
| `end_good` | No warnings (normal node) |

---

## Code Quality

### Maintainability:
- ✅ Separate function for warning generation
- ✅ Clear, self-documenting code structure
- ✅ Easy to add new warning types
- ✅ Consistent data format

### Performance:
- ✅ Warnings computed only on node click (not upfront)
- ✅ Efficient array searches with `.some()` and `.filter()`
- ✅ No impact on initial page load or analysis time

### Browser Compatibility:
- ✅ Works in all modern browsers
- ✅ Uses standard ES6 features
- ✅ No external dependencies added

---

## Future Enhancements (Optional)

### Potential Improvements:

1. **Quick Fix Suggestions**
   - Add buttons to auto-fix common issues
   - Example: "Auto-lower threshold to 15"

2. **Related Nodes**
   - Show which nodes lead to this error
   - Example: "This node is reached from: start → home"

3. **Severity Levels**
   - Categorize warnings as Error/Warning/Info
   - Use different visual emphasis

4. **Copy to Clipboard**
   - Add button to copy warning details
   - Useful for sharing with team members

5. **Filter Options**
   - Toggle which warning types to show
   - Example: "Only show critical errors"

---

## Summary

✅ **Enhanced** node details panel with error warnings  
✅ **Added** line number display for better context  
✅ **Implemented** 4 warning types with visual indicators  
✅ **Provided** actionable advice for each error type  
✅ **Maintained** consistent visual design with existing UI  
✅ **Optimized** for performance (lazy computation)  

The web interface is now **significantly more user-friendly** - developers can immediately understand what's wrong with any node and how to fix it! 🎉
