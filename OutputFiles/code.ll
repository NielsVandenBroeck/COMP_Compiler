
@.uniqprintStringuniquniqmain587 = private unnamed_addr constant [5 x i8] c"%d\n\00", align 1
@.uniqprintStringuniqmain410 = private unnamed_addr constant [4 x i8] c"2\n\00", align 1
@.uniqprintStringuniqmain48 = private unnamed_addr constant [31 x i8] c"First %d prime numbers are :\n\00", align 1
@.uniqscanStringmain2 = private unnamed_addr constant [3 x i8] c"%d\00", align 1
@.uniqprintStringmain1 = private unnamed_addr constant [45 x i8] c"Enter the number of prime numbers required\n\00", align 1
declare dso_local i32 @__isoc99_scanf(i8*, ...) #1
@.procentC = private unnamed_addr constant [3 x i8] c"%c\00", align 1
@.procentF = private unnamed_addr constant [3 x i8] c"%f\00", align 1
declare dso_local i32 @printf(i8*, ...) #1
define i32 @main() #0 {
	%n = alloca i32, align 4
	%i = alloca i32, align 4
	store i32 3, i32* %i, align 4
	%count = alloca i32, align 4
	%c = alloca i32, align 4
	call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([45 x i8], [45 x i8]* @.uniqprintStringmain1, i64 0, i64 0) )
	%uniqnmain3 = load i32, i32* %n, align 4
	call i32 (i8*, ...) @__isoc99_scanf(i8* getelementptr inbounds ([3 x i8], [3 x i8]* @.uniqscanStringmain2, i64 0, i64 0), i32* %n)
	%uniqwhileLoopConditionuniqmain41 = alloca i32, align 4
	%uniquniqmain42 = alloca i32, align 4
	store i32 1, i32* %uniquniqmain42, align 4
	%uniqnuniqmain43 = load i32, i32* %n, align 4
	%uniquniquniqmain42uniqmain44 = load i32, i32* %uniquniqmain42, align 4
	%uniquniqmain45 = icmp sge i32 %uniqnuniqmain43, %uniquniquniqmain42uniqmain44
	%uniquniqmain46= zext i1 %uniquniqmain45 to i32
	store i32 %uniquniqmain46, i32* %uniqwhileLoopConditionuniqmain41, align 4
	%uniqcheckValueReguniqmain47 = load i32, i32* %uniqwhileLoopConditionuniqmain41, align 4
	%conditionValueuniqmain4= icmp eq i32 %uniqcheckValueReguniqmain47, 1
	br i1 %conditionValueuniqmain4, label %ifStatement_uniqmain4, label %elseStatement_uniqmain4

ifStatement_uniqmain4:
	%uniqnuniqmain49 = load i32, i32* %n, align 4
	call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([31 x i8], [31 x i8]* @.uniqprintStringuniqmain48, i64 0, i64 0) , i32 %uniqnuniqmain49)
	call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @.uniqprintStringuniqmain410, i64 0, i64 0) )
	br label %endIfElseStatement_uniqmain4

elseStatement_uniqmain4:
	br label %endIfElseStatement_uniqmain4

endIfElseStatement_uniqmain4:
	store i32 2, i32* %count, align 4
br label %whileCondition_uniqmain5

whileCondition_uniqmain5:
	%uniqwhileLoopConditionuniqmain51 = alloca i32, align 4
	%uniqcountuniqmain52 = load i32, i32* %count, align 4
	%uniqnuniqmain53 = load i32, i32* %n, align 4
	%uniquniqmain54 = icmp sle i32 %uniqcountuniqmain52, %uniqnuniqmain53
	%uniquniqmain55= zext i1 %uniquniqmain54 to i32
	store i32 %uniquniqmain55, i32* %uniqwhileLoopConditionuniqmain51, align 4
	%uniqcheckValueReguniqmain56 = load i32, i32* %uniqwhileLoopConditionuniqmain51, align 4
	%conditionValueuniqmain5= icmp eq i32 %uniqcheckValueReguniqmain56, 1
	br i1 %conditionValueuniqmain5, label %whileLoop_uniqmain5, label %endwhile_uniqmain5

whileLoop_uniqmain5:
	store i32 2, i32* %c, align 4
br label %whileCondition_uniquniqmain57

whileCondition_uniquniqmain57:
	%uniqwhileLoopConditionuniquniqmain571 = alloca i32, align 4
	%uniquniquniqmain572 = alloca i32, align 4
	%uniquniquniqmain573 = alloca i32, align 4
	store i32 1, i32* %uniquniquniqmain573, align 4
	%uniqiuniquniqmain574 = load i32, i32* %i, align 4
	%uniquniquniquniqmain573uniquniqmain575 = load i32, i32* %uniquniquniqmain573, align 4
	%uniquniquniqmain576 = sub i32 %uniqiuniquniqmain574, %uniquniquniquniqmain573uniquniqmain575
	store i32 %uniquniquniqmain576, i32* %uniquniquniqmain572, align 4
	%uniqcuniquniqmain577 = load i32, i32* %c, align 4
	%uniquniquniquniqmain572uniquniqmain578 = load i32, i32* %uniquniquniqmain572, align 4
	%uniquniquniqmain579 = icmp sle i32 %uniqcuniquniqmain577, %uniquniquniquniqmain572uniquniqmain578
	%uniquniquniqmain5710= zext i1 %uniquniquniqmain579 to i32
	store i32 %uniquniquniqmain5710, i32* %uniqwhileLoopConditionuniquniqmain571, align 4
	%uniqcheckValueReguniquniqmain5711 = load i32, i32* %uniqwhileLoopConditionuniquniqmain571, align 4
	%conditionValueuniquniqmain57= icmp eq i32 %uniqcheckValueReguniquniqmain5711, 1
	br i1 %conditionValueuniquniqmain57, label %whileLoop_uniquniqmain57, label %endwhile_uniquniqmain57

whileLoop_uniquniqmain57:
	%uniqwhileLoopConditionuniquniquniqmain57121 = alloca i32, align 4
	%uniquniquniquniqmain57122 = alloca i32, align 4
	%uniqiuniquniquniqmain57123 = load i32, i32* %i, align 4
	%uniqcuniquniquniqmain57124 = load i32, i32* %c, align 4
	%uniquniquniquniqmain57125 = srem i32 %uniqiuniquniquniqmain57123, %uniqcuniquniquniqmain57124
	store i32 %uniquniquniquniqmain57125, i32* %uniquniquniquniqmain57122, align 4
	%uniquniquniquniqmain57126 = alloca i32, align 4
	store i32 0, i32* %uniquniquniquniqmain57126, align 4
	%uniquniquniquniquniqmain57122uniquniquniqmain57127 = load i32, i32* %uniquniquniquniqmain57122, align 4
	%uniquniquniquniquniqmain57126uniquniquniqmain57128 = load i32, i32* %uniquniquniquniqmain57126, align 4
	%uniquniquniquniqmain57129 = icmp eq i32 %uniquniquniquniquniqmain57122uniquniquniqmain57127, %uniquniquniquniquniqmain57126uniquniquniqmain57128
	%uniquniquniquniqmain571210= zext i1 %uniquniquniquniqmain57129 to i32
	store i32 %uniquniquniquniqmain571210, i32* %uniqwhileLoopConditionuniquniquniqmain57121, align 4
	%uniqcheckValueReguniquniquniqmain571211 = load i32, i32* %uniqwhileLoopConditionuniquniquniqmain57121, align 4
	%conditionValueuniquniquniqmain5712= icmp eq i32 %uniqcheckValueReguniquniquniqmain571211, 1
	br i1 %conditionValueuniquniquniqmain5712, label %ifStatement_uniquniquniqmain5712, label %elseStatement_uniquniquniqmain5712

ifStatement_uniquniquniqmain5712:
	br label %endwhile_uniquniqmain57
	br label %endIfElseStatement_uniquniquniqmain5712

elseStatement_uniquniquniqmain5712:
	br label %endIfElseStatement_uniquniquniqmain5712

endIfElseStatement_uniquniquniqmain5712:
	%uniquniquniqmain5713 = alloca i32, align 4
	store i32 1, i32* %uniquniquniqmain5713, align 4
	%uniqcuniquniqmain5714 = load i32, i32* %c, align 4
	%uniquniquniquniqmain5713uniquniqmain5715 = load i32, i32* %uniquniquniqmain5713, align 4
	%uniquniquniqmain5716 = add i32 %uniqcuniquniqmain5714, %uniquniquniquniqmain5713uniquniqmain5715
	store i32 %uniquniquniqmain5716, i32* %c, align 4
	br label %whileCondition_uniquniqmain57

endwhile_uniquniqmain57:
	%uniqwhileLoopConditionuniquniqmain581 = alloca i32, align 4
	%uniqcuniquniqmain582 = load i32, i32* %c, align 4
	%uniqiuniquniqmain583 = load i32, i32* %i, align 4
	%uniquniquniqmain584 = icmp eq i32 %uniqcuniquniqmain582, %uniqiuniquniqmain583
	%uniquniquniqmain585= zext i1 %uniquniquniqmain584 to i32
	store i32 %uniquniquniqmain585, i32* %uniqwhileLoopConditionuniquniqmain581, align 4
	%uniqcheckValueReguniquniqmain586 = load i32, i32* %uniqwhileLoopConditionuniquniqmain581, align 4
	%conditionValueuniquniqmain58= icmp eq i32 %uniqcheckValueReguniquniqmain586, 1
	br i1 %conditionValueuniquniqmain58, label %ifStatement_uniquniqmain58, label %elseStatement_uniquniqmain58

ifStatement_uniquniqmain58:
	%uniqiuniquniqmain588 = load i32, i32* %i, align 4
	call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([5 x i8], [5 x i8]* @.uniqprintStringuniquniqmain587, i64 0, i64 0) , i32 %uniqiuniquniqmain588)
	%uniquniquniqmain589 = alloca i32, align 4
	store i32 1, i32* %uniquniquniqmain589, align 4
	%uniqcountuniquniqmain5810 = load i32, i32* %count, align 4
	%uniquniquniquniqmain589uniquniqmain5811 = load i32, i32* %uniquniquniqmain589, align 4
	%uniquniquniqmain5812 = add i32 %uniqcountuniquniqmain5810, %uniquniquniquniqmain589uniquniqmain5811
	store i32 %uniquniquniqmain5812, i32* %count, align 4
	br label %endIfElseStatement_uniquniqmain58

elseStatement_uniquniqmain58:
	br label %endIfElseStatement_uniquniqmain58

endIfElseStatement_uniquniqmain58:
	%uniquniqmain59 = alloca i32, align 4
	store i32 1, i32* %uniquniqmain59, align 4
	%uniqiuniqmain510 = load i32, i32* %i, align 4
	%uniquniquniqmain59uniqmain511 = load i32, i32* %uniquniqmain59, align 4
	%uniquniqmain512 = add i32 %uniqiuniqmain510, %uniquniquniqmain59uniqmain511
	store i32 %uniquniqmain512, i32* %i, align 4
	br label %whileCondition_uniqmain5

endwhile_uniqmain5:
	ret i32 0
}